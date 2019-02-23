# T-Peos Spider
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.7; 28 -12.7; 31 -12.6; 34 -12.6; 37 -12.5; 41 -12.5; 45 -12.5; 49 -12.4; 54 -12.4; 60 -12.4; 66 -12.4; 72 -12.4; 79 -12.5; 87 -12.5; 96 -12.5; 106 -12.3; 116 -12.1; 128 -11.9; 141 -11.7; 155 -11.4; 170 -11.0; 187 -10.6; 206 -10.1; 227 -9.5; 249 -9.0; 274 -8.4; 302 -7.8; 332 -7.3; 365 -6.6; 402 -6.1; 442 -5.4; 486 -5.0; 535 -4.5; 588 -3.8; 647 -3.5; 712 -3.4; 783 -3.1; 861 -3.3; 947 -3.7; 1042 -4.2; 1146 -4.8; 1261 -5.2; 1387 -6.2; 1526 -7.3; 1678 -8.2; 1846 -8.8; 2031 -9.0; 2234 -8.6; 2457 -6.7; 2703 -4.2; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.3; 4788 -8.8; 5267 -12.3; 5793 -7.4; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -8.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Spider GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Spider ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.15 | -6.3 dB |
| Peaking | 846 Hz   | 0.57 | 7.3 dB  |
| Peaking | 2652 Hz  | 0.43 | -8.8 dB |
| Peaking | 3352 Hz  | 1.91 | 14.4 dB |
| Peaking | 6712 Hz  | 5.78 | 6.8 dB  |
| Peaking | 2036 Hz  | 6.03 | -0.9 dB |
| Peaking | 4113 Hz  | 7.23 | 3.7 dB  |
| Peaking | 5286 Hz  | 5.23 | -5.7 dB |
| Peaking | 6042 Hz  | 7.08 | 2.9 dB  |
| Peaking | 11806 Hz | 1.45 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Spider/T-Peos%20Spider.png)
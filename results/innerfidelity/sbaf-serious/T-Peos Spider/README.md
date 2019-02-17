# T-Peos Spider
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.8; 25 -14.7; 28 -14.7; 31 -14.7; 34 -14.6; 37 -14.6; 41 -14.5; 45 -14.5; 49 -14.5; 54 -14.4; 60 -14.4; 66 -14.4; 72 -14.5; 79 -14.5; 87 -14.5; 96 -14.5; 106 -14.4; 116 -14.1; 128 -14.0; 141 -13.7; 155 -13.4; 170 -13.0; 187 -12.6; 206 -12.2; 227 -11.6; 249 -11.0; 274 -10.5; 302 -9.9; 332 -9.3; 365 -8.7; 402 -8.1; 442 -7.4; 486 -7.1; 535 -6.6; 588 -5.9; 647 -5.5; 712 -5.4; 783 -5.1; 861 -5.4; 947 -5.7; 1042 -6.2; 1146 -6.8; 1261 -7.2; 1387 -8.3; 1526 -9.3; 1678 -10.2; 1846 -10.8; 2031 -11.0; 2234 -10.7; 2457 -8.7; 2703 -6.2; 2973 -3.1; 3270 -0.9; 3597 -0.5; 3957 -2.2; 4353 -6.3; 4788 -10.8; 5267 -14.3; 5793 -9.4; 6373 -5.2; 7010 -4.2; 7711 -6.2; 8482 -9.5; 9330 -10.4; 10263 -8.0; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Spider GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Spider ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.22 | -9.1 dB  |
| Peaking | 2111 Hz | 1.91 | -7.3 dB  |
| Peaking | 3468 Hz | 1.59 | 7.8 dB   |
| Peaking | 5129 Hz | 4.76 | -10.9 dB |
| Peaking | 9154 Hz | 5.33 | -5.2 dB  |
| Peaking | 21 Hz   | 2.73 | -1.2 dB  |
| Peaking | 192 Hz  | 1.49 | -1.0 dB  |
| Peaking | 706 Hz  | 1.35 | 2.5 dB   |
| Peaking | 2348 Hz | 0.21 | -0.5 dB  |
| Peaking | 6817 Hz | 6.04 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Spider/T-Peos%20Spider.png)
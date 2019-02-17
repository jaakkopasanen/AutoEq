# Sony XBA-Z5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.9; 25 -10.0; 28 -10.2; 31 -10.3; 34 -10.5; 37 -10.6; 41 -10.7; 45 -10.8; 49 -11.0; 54 -11.2; 60 -11.5; 66 -11.8; 72 -12.0; 79 -12.3; 87 -12.6; 96 -12.9; 106 -13.0; 116 -13.1; 128 -13.2; 141 -13.2; 155 -13.1; 170 -13.0; 187 -12.7; 206 -12.5; 227 -12.0; 249 -11.6; 274 -11.1; 302 -10.6; 332 -10.0; 365 -9.3; 402 -9.0; 442 -8.4; 486 -8.2; 535 -7.6; 588 -7.0; 647 -6.4; 712 -5.8; 783 -5.5; 861 -5.6; 947 -5.9; 1042 -6.1; 1146 -6.2; 1261 -6.4; 1387 -6.6; 1526 -6.8; 1678 -6.6; 1846 -6.0; 2031 -5.0; 2234 -4.4; 2457 -3.6; 2703 -2.7; 2973 -2.1; 3270 -0.8; 3597 -1.2; 3957 -3.8; 4353 -6.3; 4788 -6.8; 5267 -4.4; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.5; 10263 -10.5; 11289 -10.6; 12418 -8.2; 13660 -8.2; 15026 -7.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-Z5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.27 | -4.3 dB |
| Peaking | 174 Hz   | 0.63 | -4.7 dB |
| Peaking | 3186 Hz  | 2.8  | 5.3 dB  |
| Peaking | 6157 Hz  | 4.84 | 6.5 dB  |
| Peaking | 10938 Hz | 2.57 | -5.3 dB |
| Peaking | 775 Hz   | 3.58 | 1.3 dB  |
| Peaking | 1549 Hz  | 3.22 | -1.3 dB |
| Peaking | 4635 Hz  | 4.85 | -3.4 dB |
| Peaking | 4642 Hz  | 0.44 | 0.8 dB  |
| Peaking | 14311 Hz | 4.2  | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20XBA-Z5/Sony%20XBA-Z5.png)
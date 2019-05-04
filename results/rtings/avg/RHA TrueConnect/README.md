# RHA TrueConnect
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.0; 25 -15.8; 28 -15.6; 31 -15.3; 34 -15.1; 37 -14.8; 41 -14.5; 45 -14.2; 49 -14.0; 54 -13.7; 60 -13.4; 66 -13.2; 72 -13.0; 79 -12.8; 87 -12.6; 96 -12.4; 106 -12.2; 116 -12.1; 128 -11.8; 141 -11.6; 155 -11.5; 170 -11.2; 187 -10.7; 206 -10.2; 227 -9.7; 249 -9.2; 274 -8.7; 302 -8.2; 332 -7.7; 365 -7.2; 402 -6.7; 442 -6.1; 486 -5.6; 535 -5.0; 588 -4.5; 647 -4.1; 712 -3.8; 783 -3.5; 861 -3.6; 947 -4.0; 1042 -4.7; 1146 -5.5; 1261 -6.1; 1387 -6.4; 1526 -6.4; 1678 -6.4; 1846 -6.5; 2031 -6.3; 2234 -5.8; 2457 -4.9; 2703 -4.3; 2973 -2.6; 3270 -0.6; 3597 -0.5; 3957 -1.2; 4353 -2.0; 4788 -2.7; 5267 -2.7; 5793 -2.3; 6373 -2.7; 7010 -7.4; 7711 -12.2; 8482 -11.0; 9330 -9.2; 10263 -13.4; 11289 -17.6; 12418 -14.0; 13660 -7.6; 15026 -7.1; 16529 -13.0; 18182 -17.4; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA TrueConnect GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA TrueConnect ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.25 | -9.4 dB  |
| Peaking | 150 Hz   | 1.22 | -3.0 dB  |
| Peaking | 3943 Hz  | 1.32 | 6.1 dB   |
| Peaking | 11173 Hz | 2.51 | -10.9 dB |
| Peaking | 18402 Hz | 1.4  | -12.1 dB |
| Peaking | 771 Hz   | 1.49 | 3.4 dB   |
| Peaking | 1747 Hz  | 1.5  | -1.4 dB  |
| Peaking | 6202 Hz  | 4.68 | 3.8 dB   |
| Peaking | 7680 Hz  | 5.62 | -6.3 dB  |
| Peaking | 14336 Hz | 4.46 | 4.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/RHA%20TrueConnect/RHA%20TrueConnect.png)
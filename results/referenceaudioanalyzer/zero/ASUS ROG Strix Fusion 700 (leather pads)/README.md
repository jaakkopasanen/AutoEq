# ASUS ROG Strix Fusion 700 (leather pads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.6; 28 -9.6; 31 -9.6; 34 -9.6; 37 -9.7; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.2; 60 -10.5; 66 -10.9; 72 -11.2; 79 -11.5; 87 -11.8; 96 -11.9; 106 -11.9; 116 -11.9; 128 -11.6; 141 -11.3; 155 -10.8; 170 -9.9; 187 -8.5; 206 -6.7; 227 -4.2; 249 -1.7; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.1; 535 -3.7; 588 -6.3; 647 -8.3; 712 -9.2; 783 -9.7; 861 -10.6; 947 -11.6; 1042 -12.3; 1146 -12.5; 1261 -12.5; 1387 -12.5; 1526 -12.2; 1678 -12.1; 1846 -11.4; 2031 -9.9; 2234 -7.8; 2457 -5.5; 2703 -3.9; 2973 -3.9; 3270 -4.4; 3597 -3.4; 3957 -1.8; 4353 -5.1; 4788 -8.1; 5267 -8.7; 5793 -11.5; 6373 -15.3; 7010 -15.1; 7711 -9.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASUS ROG Strix Fusion 700 (leather pads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASUS ROG Strix Fusion 700 (leather pads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.24 | -2.8 dB  |
| Peaking | 146 Hz  | 0.75 | -6.7 dB  |
| Peaking | 314 Hz  | 0.86 | 10.6 dB  |
| Peaking | 1091 Hz | 1.16 | -8.0 dB  |
| Peaking | 6621 Hz | 4.83 | -10.5 dB |
| Peaking | 470 Hz  | 8.6  | 2.2 dB   |
| Peaking | 1818 Hz | 2.98 | -3.1 dB  |
| Peaking | 2744 Hz | 2.87 | 3.9 dB   |
| Peaking | 3971 Hz | 3.76 | 6.4 dB   |
| Peaking | 4772 Hz | 2.25 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -8.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASUS%20ROG%20Strix%20Fusion%20700%20(leather%20pads)/ASUS%20ROG%20Strix%20Fusion%20700%20(leather%20pads).png)
# ASUS ROG Strix Fusion 700 (fabric pads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.2; 25 -10.2; 28 -10.2; 31 -10.2; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.5; 49 -10.6; 54 -10.6; 60 -10.6; 66 -10.8; 72 -11.1; 79 -11.4; 87 -11.6; 96 -11.8; 106 -11.8; 116 -11.6; 128 -11.3; 141 -10.9; 155 -10.2; 170 -9.2; 187 -7.7; 206 -5.8; 227 -3.3; 249 -0.9; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.4; 535 -4.0; 588 -6.6; 647 -8.5; 712 -9.2; 783 -9.5; 861 -10.4; 947 -11.5; 1042 -12.3; 1146 -12.6; 1261 -12.8; 1387 -12.9; 1526 -12.7; 1678 -12.3; 1846 -11.4; 2031 -9.8; 2234 -7.8; 2457 -6.4; 2703 -5.5; 2973 -5.7; 3270 -6.4; 3597 -5.7; 3957 -4.1; 4353 -7.0; 4788 -10.3; 5267 -10.9; 5793 -11.7; 6373 -12.8; 7010 -11.1; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASUS ROG Strix Fusion 700 (fabric pads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASUS ROG Strix Fusion 700 (fabric pads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.21 | -3.6 dB |
| Peaking | 141 Hz  | 0.84 | -5.9 dB |
| Peaking | 311 Hz  | 0.83 | 10.1 dB |
| Peaking | 1121 Hz | 1.03 | -8.0 dB |
| Peaking | 6172 Hz | 3.6  | -6.7 dB |
| Peaking | 470 Hz  | 6.46 | 2.4 dB  |
| Peaking | 640 Hz  | 5.2  | -2.2 dB |
| Peaking | 1756 Hz | 3.95 | -2.3 dB |
| Peaking | 2681 Hz | 3.26 | 2.8 dB  |
| Peaking | 3891 Hz | 8.78 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | 6.0 dB  |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASUS%20ROG%20Strix%20Fusion%20700%20(fabric%20pads)/ASUS%20ROG%20Strix%20Fusion%20700%20(fabric%20pads).png)
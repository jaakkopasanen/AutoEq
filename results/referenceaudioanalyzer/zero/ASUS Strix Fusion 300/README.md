# ASUS Strix Fusion 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -14.2; 25 -14.4; 28 -14.8; 31 -15.0; 34 -15.2; 37 -15.2; 41 -15.3; 45 -15.2; 49 -15.1; 54 -14.9; 60 -14.7; 66 -14.6; 72 -14.6; 79 -14.6; 87 -14.6; 96 -14.8; 106 -14.7; 116 -14.6; 128 -14.4; 141 -14.1; 155 -13.7; 170 -13.0; 187 -11.9; 206 -10.3; 227 -8.2; 249 -5.7; 274 -2.3; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.6; 535 -3.0; 588 -4.2; 647 -5.2; 712 -6.1; 783 -6.9; 861 -7.7; 947 -8.7; 1042 -9.6; 1146 -10.2; 1261 -10.7; 1387 -10.6; 1526 -10.0; 1678 -9.2; 1846 -8.6; 2031 -7.9; 2234 -6.5; 2457 -4.7; 2703 -2.4; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -5.6; 4788 -8.4; 5267 -9.4; 5793 -10.2; 6373 -10.4; 7010 -8.9; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASUS Strix Fusion 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASUS Strix Fusion 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.27 | -7.5 dB |
| Peaking | 172 Hz  | 1.06 | -6.2 dB |
| Peaking | 348 Hz  | 0.6  | 18.3 dB |
| Peaking | 690 Hz  | 0.12 | -9.3 dB |
| Peaking | 3180 Hz | 1.6  | 13.3 dB |
| Peaking | 1285 Hz | 1.63 | -3.4 dB |
| Peaking | 1438 Hz | 0.84 | 2.6 dB  |
| Peaking | 3955 Hz | 6.64 | 4.7 dB  |
| Peaking | 6290 Hz | 0.93 | -6.5 dB |
| Peaking | 8028 Hz | 1.03 | 6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 6.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASUS%20Strix%20Fusion%20300/ASUS%20Strix%20Fusion%20300.png)
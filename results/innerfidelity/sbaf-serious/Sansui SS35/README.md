# Sansui SS35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.7; 116 -0.6; 128 -0.5; 141 -0.6; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -1.0; 302 -3.7; 332 -6.6; 365 -9.1; 402 -11.2; 442 -12.3; 486 -12.5; 535 -12.2; 588 -11.9; 647 -12.0; 712 -12.1; 783 -12.3; 861 -12.8; 947 -13.2; 1042 -13.8; 1146 -14.2; 1261 -14.5; 1387 -14.6; 1526 -14.0; 1678 -12.9; 1846 -11.8; 2031 -12.2; 2234 -14.3; 2457 -13.0; 2703 -9.7; 2973 -5.3; 3270 -1.7; 3597 -0.7; 3957 -6.1; 4353 -10.1; 4788 -9.4; 5267 -5.4; 5793 -2.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sansui SS35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 108 Hz  | 0.13 | 6.9 dB   |
| Peaking | 460 Hz  | 1.8  | -9.1 dB  |
| Peaking | 1126 Hz | 0.79 | -10.0 dB |
| Peaking | 2339 Hz | 4.27 | -5.5 dB  |
| Peaking | 3373 Hz | 4.65 | 8.6 dB   |
| Peaking | 20 Hz   | 2.56 | 1.1 dB   |
| Peaking | 263 Hz  | 3.44 | 2.7 dB   |
| Peaking | 357 Hz  | 4.56 | -1.9 dB  |
| Peaking | 4527 Hz | 5.57 | -5.1 dB  |
| Peaking | 6156 Hz | 4.14 | 6.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -6.7 dB |
| Peaking | 1000 Hz  | 1.41 | -5.6 dB |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35/Sansui%20SS35.png)
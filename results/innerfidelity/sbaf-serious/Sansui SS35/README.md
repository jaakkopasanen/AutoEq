# Sansui SS35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -2.1; 402 -4.2; 442 -5.3; 486 -5.4; 535 -5.1; 588 -4.9; 647 -4.9; 712 -5.1; 783 -5.2; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.1; 1261 -7.5; 1387 -7.6; 1526 -7.0; 1678 -5.9; 1846 -4.7; 2031 -5.1; 2234 -7.3; 2457 -6.0; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sansui SS35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.21 | 6.1 dB  |
| Peaking | 200 Hz  | 1.02 | 3.1 dB  |
| Peaking | 315 Hz  | 3.34 | 3.2 dB  |
| Peaking | 3370 Hz | 2.53 | 6.4 dB  |
| Peaking | 5715 Hz | 2.88 | 6.0 dB  |
| Peaking | 106 Hz  | 2.88 | 0.2 dB  |
| Peaking | 1376 Hz | 2.06 | -3.9 dB |
| Peaking | 1780 Hz | 1.07 | 2.9 dB  |
| Peaking | 2312 Hz | 6.34 | -4.2 dB |
| Peaking | 8292 Hz | 3.69 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.4 dB  |
| Peaking | 250 Hz   | 1.41 | 5.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35/Sansui%20SS35.png)
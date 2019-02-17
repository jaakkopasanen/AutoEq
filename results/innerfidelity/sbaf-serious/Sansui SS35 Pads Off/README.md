# Sansui SS35 Pads Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.1; 60 -1.7; 66 -2.3; 72 -2.6; 79 -2.9; 87 -3.2; 96 -3.6; 106 -3.6; 116 -3.7; 128 -3.7; 141 -3.9; 155 -4.0; 170 -3.5; 187 -3.5; 206 -3.2; 227 -2.4; 249 -2.0; 274 -1.8; 302 -2.1; 332 -3.1; 365 -4.0; 402 -4.6; 442 -4.8; 486 -5.1; 535 -4.8; 588 -3.8; 647 -3.3; 712 -3.3; 783 -3.7; 861 -4.8; 947 -5.8; 1042 -6.9; 1146 -7.3; 1261 -7.1; 1387 -6.5; 1526 -4.7; 1678 -3.2; 1846 -2.1; 2031 -2.8; 2234 -5.1; 2457 -3.8; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sansui SS35 Pads Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sansui SS35 Pads Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.38 | 6.2 dB  |
| Peaking | 266 Hz  | 1.53 | 4.1 dB  |
| Peaking | 682 Hz  | 3.49 | 3.0 dB  |
| Peaking | 3361 Hz | 1.19 | 6.0 dB  |
| Peaking | 5656 Hz | 2.84 | 4.5 dB  |
| Peaking | 1248 Hz | 2.78 | -2.8 dB |
| Peaking | 1917 Hz | 1.85 | 3.6 dB  |
| Peaking | 2287 Hz | 5.48 | -4.6 dB |
| Peaking | 6560 Hz | 6.49 | 2.4 dB  |
| Peaking | 7695 Hz | 1.83 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sansui%20SS35%20Pads%20Off/Sansui%20SS35%20Pads%20Off.png)
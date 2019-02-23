# Polk Audio UltraFocus 8000 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.3; 25 -12.0; 28 -11.7; 31 -11.4; 34 -11.2; 37 -11.1; 41 -10.9; 45 -10.6; 49 -10.3; 54 -10.1; 60 -9.8; 66 -9.4; 72 -9.2; 79 -9.2; 87 -9.3; 96 -9.3; 106 -9.1; 116 -8.8; 128 -8.8; 141 -8.7; 155 -8.5; 170 -8.2; 187 -8.4; 206 -8.4; 227 -8.0; 249 -7.7; 274 -7.7; 302 -8.2; 332 -8.1; 365 -7.5; 402 -8.0; 442 -8.1; 486 -8.3; 535 -8.1; 588 -7.7; 647 -8.0; 712 -7.7; 783 -7.0; 861 -7.1; 947 -6.7; 1042 -6.7; 1146 -6.1; 1261 -5.2; 1387 -5.7; 1526 -6.1; 1678 -6.5; 1846 -6.6; 2031 -6.9; 2234 -6.5; 2457 -5.3; 2703 -3.9; 2973 -2.9; 3270 -1.8; 3597 -0.5; 3957 -1.9; 4353 -2.7; 4788 -7.0; 5267 -5.1; 5793 -4.8; 6373 -2.3; 7010 -3.9; 7711 -6.2; 8482 -6.6; 9330 -8.0; 10263 -6.7; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.8; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.72 | -5.4 dB |
| Peaking | 31 Hz   | 0.57 | -2.4 dB |
| Peaking | 153 Hz  | 0.23 | -1.7 dB |
| Peaking | 3518 Hz | 2.7  | 6.1 dB  |
| Peaking | 6496 Hz | 6.85 | 4.3 dB  |
| Peaking | 617 Hz  | 1.79 | -0.7 dB |
| Peaking | 1545 Hz | 1.51 | 2.2 dB  |
| Peaking | 1661 Hz | 3.28 | -1.9 dB |
| Peaking | 2064 Hz | 4.77 | -1.6 dB |
| Peaking | 9357 Hz | 5.55 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFocus%208000%20NC/Polk%20Audio%20UltraFocus%208000%20NC.png)
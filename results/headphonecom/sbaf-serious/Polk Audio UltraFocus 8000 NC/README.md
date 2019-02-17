# Polk Audio UltraFocus 8000 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.0; 25 -11.8; 28 -11.5; 31 -11.2; 34 -11.0; 37 -10.8; 41 -10.6; 45 -10.3; 49 -10.1; 54 -9.9; 60 -9.5; 66 -9.1; 72 -8.9; 79 -8.9; 87 -9.0; 96 -9.0; 106 -8.8; 116 -8.6; 128 -8.6; 141 -8.4; 155 -8.3; 170 -7.9; 187 -8.1; 206 -8.2; 227 -7.8; 249 -7.5; 274 -7.4; 302 -7.9; 332 -7.8; 365 -7.2; 402 -7.8; 442 -7.9; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.7; 712 -7.4; 783 -6.8; 861 -6.9; 947 -6.5; 1042 -6.5; 1146 -5.9; 1261 -5.0; 1387 -5.4; 1526 -5.8; 1678 -6.2; 1846 -6.4; 2031 -6.7; 2234 -6.2; 2457 -5.0; 2703 -3.6; 2973 -2.6; 3270 -1.5; 3597 -0.5; 3957 -1.6; 4353 -2.7; 4788 -6.7; 5267 -4.9; 5793 -4.6; 6373 -2.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.72 | -5.2 dB |
| Peaking | 32 Hz   | 0.6  | -2.1 dB |
| Peaking | 132 Hz  | 0.23 | -1.5 dB |
| Peaking | 3501 Hz | 2.47 | 6.1 dB  |
| Peaking | 6463 Hz | 6.49 | 4.4 dB  |
| Peaking | 541 Hz  | 2.6  | -0.6 dB |
| Peaking | 1132 Hz | 4.39 | -0.8 dB |
| Peaking | 1237 Hz | 3.25 | 2.0 dB  |
| Peaking | 2041 Hz | 6.11 | -1.0 dB |
| Peaking | 9337 Hz | 5.6  | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFocus%208000%20NC/Polk%20Audio%20UltraFocus%208000%20NC.png)
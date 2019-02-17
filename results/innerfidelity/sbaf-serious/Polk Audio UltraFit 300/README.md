# Polk Audio UltraFit 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.7; 25 -16.7; 28 -16.7; 31 -16.7; 34 -16.7; 37 -16.7; 41 -16.8; 45 -16.8; 49 -16.8; 54 -16.9; 60 -17.0; 66 -17.1; 72 -17.2; 79 -17.3; 87 -17.4; 96 -17.5; 106 -17.4; 116 -17.2; 128 -17.1; 141 -17.0; 155 -16.7; 170 -16.4; 187 -15.9; 206 -15.5; 227 -14.9; 249 -14.4; 274 -13.8; 302 -13.1; 332 -12.5; 365 -11.8; 402 -11.2; 442 -10.3; 486 -9.8; 535 -9.1; 588 -8.2; 647 -7.7; 712 -7.3; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.9; 1261 -7.1; 1387 -7.7; 1526 -8.4; 1678 -9.0; 1846 -9.0; 2031 -9.0; 2234 -8.7; 2457 -7.3; 2703 -6.5; 2973 -5.3; 3270 -3.9; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.5  | -9.8 dB |
| Peaking | 50 Hz   | 0.28 | -9.4 dB |
| Peaking | 191 Hz  | 0.64 | -4.9 dB |
| Peaking | 2061 Hz | 1.98 | -3.8 dB |
| Peaking | 4577 Hz | 1.3  | 7.2 dB  |
| Peaking | 848 Hz  | 2.37 | 1.7 dB  |
| Peaking | 2157 Hz | 0.07 | -0.2 dB |
| Peaking | 6269 Hz | 4.1  | 2.8 dB  |
| Peaking | 6634 Hz | 4.04 | 1.2 dB  |
| Peaking | 7500 Hz | 2.05 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -8.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%20300/Polk%20Audio%20UltraFit%20300.png)
# Polk Audio UltraFit 2000 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.8; 79 -2.9; 87 -4.0; 96 -5.1; 106 -5.6; 116 -5.9; 128 -6.1; 141 -6.1; 155 -6.0; 170 -5.7; 187 -5.3; 206 -5.0; 227 -4.6; 249 -4.2; 274 -3.7; 302 -3.2; 332 -2.2; 365 -1.9; 402 -1.3; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -1.0; 947 -4.6; 1042 -7.6; 1146 -8.5; 1261 -9.2; 1387 -9.6; 1526 -9.7; 1678 -10.0; 1846 -10.4; 2031 -10.1; 2234 -9.0; 2457 -6.7; 2703 -4.8; 2973 -3.1; 3270 -2.9; 3597 -4.0; 3957 -4.4; 4353 -3.2; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -10.6; 9330 -11.5; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.71 | 7.0 dB   |
| Peaking | 666 Hz  | 0.76 | 8.8 dB   |
| Peaking | 1431 Hz | 0.93 | -8.1 dB  |
| Peaking | 6008 Hz | 0.74 | 7.9 dB   |
| Peaking | 8835 Hz | 2.22 | -10.3 dB |
| Peaking | 65 Hz   | 3.61 | 2.3 dB   |
| Peaking | 122 Hz  | 1.76 | -1.6 dB  |
| Peaking | 2165 Hz | 3.35 | -2.9 dB  |
| Peaking | 3168 Hz | 1.39 | 3.4 dB   |
| Peaking | 3908 Hz | 3.37 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 7.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20A/Polk%20Audio%20UltraFit%202000%20sample%20A.png)
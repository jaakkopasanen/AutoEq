# Lenntek Pro Series
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -0.8; 54 -1.0; 60 -1.4; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.9; 96 -3.4; 106 -3.7; 116 -3.9; 128 -4.3; 141 -4.6; 155 -4.8; 170 -5.0; 187 -5.1; 206 -5.2; 227 -5.3; 249 -5.4; 274 -5.3; 302 -5.4; 332 -5.3; 365 -5.2; 402 -5.1; 442 -5.0; 486 -5.1; 535 -5.1; 588 -4.7; 647 -4.7; 712 -5.0; 783 -5.0; 861 -5.5; 947 -6.1; 1042 -6.9; 1146 -7.6; 1261 -8.4; 1387 -9.6; 1526 -10.9; 1678 -12.1; 1846 -13.1; 2031 -13.3; 2234 -11.9; 2457 -8.5; 2703 -5.2; 2973 -2.4; 3270 -1.7; 3597 -2.4; 3957 -5.4; 4353 -10.2; 4788 -6.5; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenntek Pro Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.38 | 6.3 dB   |
| Peaking | 1052 Hz | 0.55 | 7.7 dB   |
| Peaking | 1983 Hz | 0.58 | -14.1 dB |
| Peaking | 3081 Hz | 2.26 | 12.9 dB  |
| Peaking | 5920 Hz | 2.94 | 9.2 dB   |
| Peaking | 2029 Hz | 8.63 | -0.8 dB  |
| Peaking | 3781 Hz | 6.31 | 3.7 dB   |
| Peaking | 4391 Hz | 4.16 | -5.3 dB  |
| Peaking | 5150 Hz | 9.64 | 3.9 dB   |
| Peaking | 7686 Hz | 0.2  | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lenntek%20Pro%20Series/Lenntek%20Pro%20Series.png)
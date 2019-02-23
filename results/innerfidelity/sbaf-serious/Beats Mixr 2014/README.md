# Beats Mixr 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.8; 25 -8.2; 28 -8.6; 31 -8.9; 34 -9.1; 37 -9.3; 41 -9.5; 45 -9.6; 49 -9.8; 54 -10.0; 60 -10.2; 66 -10.3; 72 -10.6; 79 -10.7; 87 -10.9; 96 -11.3; 106 -11.6; 116 -11.3; 128 -11.3; 141 -11.7; 155 -12.1; 170 -11.7; 187 -12.0; 206 -12.0; 227 -11.7; 249 -10.8; 274 -9.2; 302 -7.7; 332 -6.8; 365 -4.4; 402 -3.1; 442 -2.0; 486 -3.0; 535 -3.6; 588 -4.2; 647 -4.9; 712 -5.5; 783 -5.8; 861 -6.2; 947 -6.3; 1042 -6.3; 1146 -6.1; 1261 -5.8; 1387 -5.9; 1526 -6.2; 1678 -6.6; 1846 -6.7; 2031 -6.9; 2234 -7.4; 2457 -7.5; 2703 -8.1; 2973 -7.5; 3270 -6.6; 3597 -4.7; 3957 -3.3; 4353 -2.4; 4788 -6.0; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Mixr 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Mixr 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.93 | -1.7 dB |
| Peaking | 104 Hz  | 0.63 | -3.8 dB |
| Peaking | 219 Hz  | 1.18 | -4.2 dB |
| Peaking | 434 Hz  | 1.68 | 5.8 dB  |
| Peaking | 5825 Hz | 2.94 | 6.5 dB  |
| Peaking | 1322 Hz | 5.87 | 0.7 dB  |
| Peaking | 2825 Hz | 2.03 | -2.4 dB |
| Peaking | 4279 Hz | 2.63 | 4.5 dB  |
| Peaking | 4765 Hz | 7.56 | -4.9 dB |
| Peaking | 8157 Hz | 3.45 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Mixr%202014/Beats%20Mixr%202014.png)
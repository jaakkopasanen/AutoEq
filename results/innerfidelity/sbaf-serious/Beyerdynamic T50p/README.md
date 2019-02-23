# Beyerdynamic T50p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.0; 28 -1.7; 31 -2.4; 34 -3.1; 37 -3.6; 41 -4.3; 45 -4.9; 49 -5.4; 54 -6.0; 60 -6.6; 66 -7.1; 72 -7.5; 79 -7.8; 87 -8.1; 96 -8.5; 106 -7.8; 116 -7.4; 128 -7.5; 141 -7.4; 155 -7.0; 170 -6.9; 187 -8.7; 206 -10.5; 227 -11.7; 249 -12.3; 274 -12.3; 302 -12.7; 332 -13.2; 365 -13.1; 402 -12.9; 442 -12.6; 486 -12.6; 535 -12.2; 588 -11.7; 647 -11.4; 712 -10.6; 783 -10.0; 861 -10.0; 947 -10.0; 1042 -9.8; 1146 -9.4; 1261 -9.1; 1387 -9.0; 1526 -9.0; 1678 -8.6; 1846 -7.6; 2031 -6.0; 2234 -3.7; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -9.6; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 80 Hz   | 0.69 | -10.0 dB |
| Peaking | 129 Hz  | 0.22 | 22.8 dB  |
| Peaking | 283 Hz  | 0.26 | -22.5 dB |
| Peaking | 3809 Hz | 0.67 | 8.9 dB   |
| Peaking | 9030 Hz | 3.23 | -5.6 dB  |
| Peaking | 19 Hz   | 2.37 | 1.3 dB   |
| Peaking | 100 Hz  | 4.92 | -0.4 dB  |
| Peaking | 1733 Hz | 3.08 | -2.0 dB  |
| Peaking | 2514 Hz | 5.58 | 2.9 dB   |
| Peaking | 6148 Hz | 7.7  | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)
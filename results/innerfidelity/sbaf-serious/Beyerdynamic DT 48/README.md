# Beyerdynamic DT 48
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -7.3; 79 -13.8; 87 -12.5; 96 -10.1; 106 -10.1; 116 -9.8; 128 -9.2; 141 -8.6; 155 -7.7; 170 -8.5; 187 -8.3; 206 -7.8; 227 -7.2; 249 -6.6; 274 -6.0; 302 -5.3; 332 -4.8; 365 -4.4; 402 -3.8; 442 -2.7; 486 -1.8; 535 -0.7; 588 -0.5; 647 -0.7; 712 -2.4; 783 -3.1; 861 -3.8; 947 -5.5; 1042 -7.2; 1146 -9.1; 1261 -10.2; 1387 -10.9; 1526 -11.9; 1678 -13.0; 1846 -13.4; 2031 -13.1; 2234 -12.2; 2457 -9.3; 2703 -6.5; 2973 -4.6; 3270 -4.2; 3597 -2.3; 3957 -1.1; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -11.2; 8482 -16.1; 9330 -12.9; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.6; 16529 -15.7; 18182 -16.7; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.55 | 7.5 dB   |
| Peaking | 1843 Hz  | 1.03 | -18.5 dB |
| Peaking | 4017 Hz  | 0.15 | 11.6 dB  |
| Peaking | 8590 Hz  | 3.03 | -18.1 dB |
| Peaking | 17362 Hz | 0.72 | -14.5 dB |
| Peaking | 65 Hz    | 1.98 | 10.4 dB  |
| Peaking | 79 Hz    | 3.6  | -11.5 dB |
| Peaking | 116 Hz   | 0.62 | -3.7 dB  |
| Peaking | 576 Hz   | 1.88 | 3.9 dB   |
| Peaking | 1170 Hz  | 3.61 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 6.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.7 dB |
| Peaking | 4000 Hz  | 1.41 | 10.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -8.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048/Beyerdynamic%20DT%2048.png)
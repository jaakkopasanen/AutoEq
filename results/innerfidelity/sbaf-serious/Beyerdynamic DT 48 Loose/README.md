# Beyerdynamic DT 48 Loose
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.3; 87 -2.1; 96 -1.7; 106 -3.9; 116 -5.0; 128 -6.4; 141 -7.4; 155 -8.2; 170 -9.0; 187 -10.3; 206 -10.8; 227 -10.5; 249 -10.1; 274 -9.7; 302 -9.5; 332 -8.4; 365 -7.8; 402 -6.6; 442 -5.1; 486 -4.1; 535 -3.1; 588 -1.6; 647 -1.8; 712 -2.8; 783 -3.1; 861 -4.1; 947 -5.0; 1042 -6.7; 1146 -8.7; 1261 -10.1; 1387 -10.9; 1526 -12.0; 1678 -13.1; 1846 -13.3; 2031 -13.2; 2234 -12.0; 2457 -9.0; 2703 -6.3; 2973 -5.2; 3270 -4.9; 3597 -3.8; 3957 -2.4; 4353 -2.5; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.1; 8482 -13.3; 9330 -10.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.8; 16529 -15.1; 18182 -14.0; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 Loose GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 Loose ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.77 | 7.3 dB   |
| Peaking | 1909 Hz  | 1.84 | -9.9 dB  |
| Peaking | 7370 Hz  | 0.57 | 12.7 dB  |
| Peaking | 8495 Hz  | 2.08 | -18.2 dB |
| Peaking | 17050 Hz | 0.92 | -10.9 dB |
| Peaking | 22 Hz    | 3.2  | 2.5 dB   |
| Peaking | 90 Hz    | 1.69 | 3.8 dB   |
| Peaking | 231 Hz   | 0.7  | -5.5 dB  |
| Peaking | 620 Hz   | 1.13 | 6.5 dB   |
| Peaking | 1284 Hz  | 2.67 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20Loose/Beyerdynamic%20DT%2048%20Loose.png)
# Beyerdynamic DT 48 E pad holes c
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -6.2; 79 -10.4; 87 -7.7; 96 -6.3; 106 -8.6; 116 -8.0; 128 -7.5; 141 -7.0; 155 -6.1; 170 -7.0; 187 -6.7; 206 -6.2; 227 -5.5; 249 -4.9; 274 -4.2; 302 -3.5; 332 -2.9; 365 -2.3; 402 -1.4; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -1.7; 861 -3.8; 947 -5.4; 1042 -7.1; 1146 -8.1; 1261 -8.6; 1387 -9.1; 1526 -10.0; 1678 -11.2; 1846 -11.4; 2031 -11.4; 2234 -10.1; 2457 -7.1; 2703 -4.4; 2973 -3.0; 3270 -2.8; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.4; 8482 -13.9; 9330 -11.1; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.8; 16529 -13.1; 18182 -10.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E pad holes c GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E pad holes c ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 1.13 | 7.4 dB   |
| Peaking | 512 Hz   | 1.56 | 7.1 dB   |
| Peaking | 5220 Hz  | 1.5  | 7.6 dB   |
| Peaking | 8505 Hz  | 4.61 | -10.0 dB |
| Peaking | 16775 Hz | 1.74 | -7.4 dB  |
| Peaking | 65 Hz    | 2.85 | 5.4 dB   |
| Peaking | 78 Hz    | 5.7  | -7.7 dB  |
| Peaking | 114 Hz   | 2.92 | -2.6 dB  |
| Peaking | 737 Hz   | 5.27 | 3.4 dB   |
| Peaking | 1747 Hz  | 2.18 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 7.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c/Beyerdynamic%20DT%2048%20E%20pad%20holes%20c.png)
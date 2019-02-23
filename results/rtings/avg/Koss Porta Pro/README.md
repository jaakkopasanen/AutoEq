# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.1; 34 -2.0; 37 -2.8; 41 -3.8; 45 -4.6; 49 -5.4; 54 -6.1; 60 -6.9; 66 -7.6; 72 -8.2; 79 -8.7; 87 -9.3; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.6; 141 -10.7; 155 -10.6; 170 -10.5; 187 -10.2; 206 -9.8; 227 -9.3; 249 -8.9; 274 -8.7; 302 -8.5; 332 -8.2; 365 -7.9; 402 -7.6; 442 -7.4; 486 -7.1; 535 -6.7; 588 -6.4; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.8; 947 -4.7; 1042 -4.8; 1146 -5.1; 1261 -5.6; 1387 -6.2; 1526 -6.9; 1678 -7.5; 1846 -8.3; 2031 -8.8; 2234 -8.4; 2457 -7.2; 2703 -5.8; 2973 -5.7; 3270 -6.1; 3597 -5.5; 3957 -1.2; 4353 -0.5; 4788 -3.4; 5267 -8.6; 5793 -4.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.95 | 6.7 dB   |
| Peaking | 133 Hz  | 0.72 | -4.6 dB  |
| Peaking | 4387 Hz | 3.23 | 12.1 dB  |
| Peaking | 5319 Hz | 1.7  | -10.3 dB |
| Peaking | 6234 Hz | 3.32 | 10.9 dB  |
| Peaking | 370 Hz  | 1.22 | -0.5 dB  |
| Peaking | 965 Hz  | 1.23 | 2.3 dB   |
| Peaking | 2030 Hz | 1.97 | -2.7 dB  |
| Peaking | 2746 Hz | 5.27 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)
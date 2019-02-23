# Koss UR-20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.2; 25 -4.6; 28 -5.1; 31 -5.4; 34 -5.5; 37 -5.5; 41 -5.4; 45 -5.4; 49 -5.5; 54 -5.6; 60 -5.8; 66 -6.1; 72 -6.3; 79 -6.5; 87 -6.8; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.1; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.4; 274 -8.6; 302 -8.8; 332 -9.2; 365 -9.7; 402 -10.2; 442 -10.6; 486 -10.8; 535 -10.2; 588 -9.7; 647 -9.4; 712 -8.6; 783 -7.4; 861 -6.0; 947 -6.8; 1042 -5.6; 1146 -3.3; 1261 -0.9; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.5; 3957 -8.2; 4353 -9.6; 4788 -7.3; 5267 -6.1; 5793 -9.2; 6373 -10.2; 7010 -9.1; 7711 -12.9; 8482 -15.0; 9330 -10.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR-20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR-20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 152 Hz   | 1.24 | -2.4 dB |
| Peaking | 522 Hz   | 0.92 | -4.8 dB |
| Peaking | 1851 Hz  | 0.85 | 7.5 dB  |
| Peaking | 8054 Hz  | 2.44 | -8.4 dB |
| Peaking | 1952 Hz  | 4.78 | -1.4 dB |
| Peaking | 3439 Hz  | 2.75 | 5.2 dB  |
| Peaking | 4148 Hz  | 3.86 | -7.3 dB |
| Peaking | 10428 Hz | 5.39 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20UR-20/Koss%20UR-20.png)
# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.1; 41 -1.8; 45 -2.4; 49 -2.9; 54 -3.4; 60 -4.0; 66 -4.6; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.4; 106 -6.8; 116 -7.2; 128 -7.5; 141 -7.8; 155 -8.0; 170 -8.0; 187 -7.8; 206 -7.6; 227 -7.4; 249 -7.2; 274 -7.1; 302 -7.1; 332 -7.0; 365 -6.8; 402 -6.8; 442 -6.9; 486 -6.9; 535 -6.7; 588 -6.6; 647 -6.5; 712 -6.4; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.5; 1526 -7.7; 1678 -7.8; 1846 -7.8; 2031 -7.8; 2234 -6.4; 2457 -6.5; 2703 -6.6; 2973 -7.1; 3270 -6.7; 3597 -4.9; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.6; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.0; 18182 -15.0; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.62 | 6.3 dB   |
| Peaking | 146 Hz   | 0.94 | -2.0 dB  |
| Peaking | 4113 Hz  | 0.59 | -4.2 dB  |
| Peaking | 4732 Hz  | 1.47 | 10.9 dB  |
| Peaking | 19533 Hz | 1.05 | -12.9 dB |
| Peaking | 3251 Hz  | 8.3  | -1.3 dB  |
| Peaking | 8661 Hz  | 5    | -5.9 dB  |
| Peaking | 8762 Hz  | 1.47 | 2.0 dB   |
| Peaking | 15114 Hz | 1.76 | 2.2 dB   |
| Peaking | 17525 Hz | 2.15 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elear/Focal%20Elear.png)
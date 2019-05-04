# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.3; 41 -2.0; 45 -2.6; 49 -3.1; 54 -3.7; 60 -4.3; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.2; 96 -6.6; 106 -6.9; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.1; 170 -8.1; 187 -8.0; 206 -7.9; 227 -7.7; 249 -7.5; 274 -7.5; 302 -7.4; 332 -7.3; 365 -7.2; 402 -7.2; 442 -7.2; 486 -7.3; 535 -7.2; 588 -7.0; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.8; 947 -6.9; 1042 -7.0; 1146 -7.2; 1261 -7.6; 1387 -8.0; 1526 -8.3; 1678 -8.4; 1846 -8.5; 2031 -8.6; 2234 -7.8; 2457 -7.7; 2703 -7.6; 2973 -7.6; 3270 -6.8; 3597 -5.2; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.0; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.2; 18182 -15.2; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.59 | 6.3 dB   |
| Peaking | 151 Hz   |  0.73 | -2.1 dB  |
| Peaking | 3491 Hz  |  0.6  | -5.0 dB  |
| Peaking | 4635 Hz  |  1.42 | 11.3 dB  |
| Peaking | 19521 Hz |  1.02 | -13.1 dB |
| Peaking | 6177 Hz  | 10.22 | -1.9 dB  |
| Peaking | 6639 Hz  |  7.43 | 2.9 dB   |
| Peaking | 8618 Hz  |  6.45 | -3.8 dB  |
| Peaking | 15629 Hz |  1.03 | 2.8 dB   |
| Peaking | 17416 Hz |  1.85 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elear/Focal%20Elear.png)
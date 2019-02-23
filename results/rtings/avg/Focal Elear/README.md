# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.5; 41 -2.2; 45 -2.8; 49 -3.3; 54 -3.8; 60 -4.4; 66 -5.0; 72 -5.6; 79 -6.0; 87 -6.5; 96 -6.8; 106 -7.2; 116 -7.6; 128 -7.9; 141 -8.2; 155 -8.3; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.8; 249 -7.6; 274 -7.5; 302 -7.5; 332 -7.4; 365 -7.2; 402 -7.2; 442 -7.3; 486 -7.3; 535 -7.1; 588 -6.9; 647 -6.9; 712 -6.7; 783 -6.7; 861 -6.7; 947 -6.8; 1042 -6.9; 1146 -7.0; 1261 -7.3; 1387 -7.9; 1526 -8.1; 1678 -8.2; 1846 -8.2; 2031 -8.2; 2234 -6.8; 2457 -6.8; 2703 -7.0; 2973 -7.5; 3270 -7.1; 3597 -5.2; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -9.7; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.4; 18182 -15.4; 20000 -19.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.59 | 6.3 dB   |
| Peaking | 148 Hz   |  0.72 | -2.3 dB  |
| Peaking | 3943 Hz  |  0.56 | -4.5 dB  |
| Peaking | 4693 Hz  |  1.49 | 11.2 dB  |
| Peaking | 19443 Hz |  1.04 | -13.3 dB |
| Peaking | 6183 Hz  | 11.12 | -3.4 dB  |
| Peaking | 6620 Hz  |  6.16 | 3.3 dB   |
| Peaking | 8804 Hz  |  6.73 | -4.7 dB  |
| Peaking | 15583 Hz |  0.81 | 2.9 dB   |
| Peaking | 17497 Hz |  1.94 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elear/Focal%20Elear.png)
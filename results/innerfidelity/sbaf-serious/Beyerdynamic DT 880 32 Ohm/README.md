# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.8; 37 -2.2; 41 -2.7; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.4; 66 -4.7; 72 -4.5; 79 -4.8; 87 -6.1; 96 -6.8; 106 -7.3; 116 -7.7; 128 -8.1; 141 -8.5; 155 -8.7; 170 -8.8; 187 -9.0; 206 -9.1; 227 -9.0; 249 -8.9; 274 -8.9; 302 -8.7; 332 -8.7; 365 -8.6; 402 -8.3; 442 -7.8; 486 -7.6; 535 -7.7; 588 -7.3; 647 -7.2; 712 -7.0; 783 -6.5; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -5.9; 1387 -6.1; 1526 -6.7; 1678 -7.3; 1846 -7.8; 2031 -7.6; 2234 -7.6; 2457 -6.8; 2703 -7.6; 2973 -7.4; 3270 -7.3; 3597 -7.1; 3957 -7.2; 4353 -6.9; 4788 -4.4; 5267 -0.6; 5793 -0.5; 6373 -6.6; 7010 -8.2; 7711 -9.0; 8482 -11.0; 9330 -10.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  0.52 | 6.1 dB  |
| Peaking | 76 Hz    |  4.46 | 1.3 dB  |
| Peaking | 195 Hz   |  0.55 | -2.9 dB |
| Peaking | 5509 Hz  |  5.4  | 7.7 dB  |
| Peaking | 8540 Hz  |  2.81 | -5.0 dB |
| Peaking | 1350 Hz  |  1.78 | 1.4 dB  |
| Peaking | 1786 Hz  |  2.1  | -1.6 dB |
| Peaking | 3915 Hz  |  1.21 | -1.1 dB |
| Peaking | 5023 Hz  | 10.04 | 2.3 dB  |
| Peaking | 10645 Hz |  5.5  | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)
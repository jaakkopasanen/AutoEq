# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.4; 41 -1.9; 45 -2.3; 49 -2.6; 54 -3.0; 60 -3.6; 66 -3.9; 72 -3.7; 79 -4.0; 87 -5.2; 96 -6.0; 106 -6.5; 116 -6.8; 128 -7.3; 141 -7.6; 155 -7.9; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.1; 249 -8.1; 274 -8.0; 302 -7.9; 332 -7.9; 365 -7.7; 402 -7.5; 442 -6.9; 486 -6.8; 535 -6.8; 588 -6.5; 647 -6.3; 712 -6.2; 783 -5.7; 861 -5.9; 947 -5.8; 1042 -5.6; 1146 -5.2; 1261 -5.0; 1387 -5.3; 1526 -5.8; 1678 -6.5; 1846 -6.9; 2031 -6.8; 2234 -6.7; 2457 -6.0; 2703 -6.7; 2973 -6.6; 3270 -6.5; 3597 -6.3; 3957 -6.4; 4353 -6.0; 4788 -3.6; 5267 -0.5; 5793 -0.5; 6373 -5.8; 7010 -7.4; 7711 -8.2; 8482 -10.1; 9330 -10.0; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.28 | 6.2 dB  |
| Peaking | 172 Hz  |  0.64 | -2.6 dB |
| Peaking | 1122 Hz |  1.88 | 1.5 dB  |
| Peaking | 5478 Hz |  4.45 | 7.3 dB  |
| Peaking | 8618 Hz |  3.31 | -4.4 dB |
| Peaking | 173 Hz  |  5.06 | 0.2 dB  |
| Peaking | 1898 Hz |  5.18 | -0.8 dB |
| Peaking | 6745 Hz | 10.22 | -1.6 dB |
| Peaking | 9287 Hz |  7.09 | -2.3 dB |
| Peaking | 9720 Hz |  2.51 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)
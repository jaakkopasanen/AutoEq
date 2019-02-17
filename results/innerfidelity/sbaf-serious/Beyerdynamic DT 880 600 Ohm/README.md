# Beyerdynamic DT 880 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.2; 45 -3.5; 49 -3.8; 54 -4.3; 60 -4.8; 66 -5.0; 72 -4.6; 79 -5.2; 87 -6.3; 96 -7.0; 106 -7.4; 116 -7.7; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.8; 187 -8.9; 206 -9.1; 227 -9.0; 249 -9.0; 274 -8.9; 302 -8.7; 332 -8.7; 365 -8.5; 402 -8.4; 442 -7.8; 486 -7.7; 535 -7.8; 588 -7.5; 647 -7.3; 712 -7.2; 783 -6.8; 861 -6.9; 947 -6.7; 1042 -6.3; 1146 -6.0; 1261 -5.8; 1387 -6.1; 1526 -6.5; 1678 -7.1; 1846 -7.5; 2031 -7.2; 2234 -6.9; 2457 -6.0; 2703 -6.4; 2973 -6.1; 3270 -5.8; 3597 -5.4; 3957 -5.5; 4353 -6.2; 4788 -5.4; 5267 -5.6; 5793 -8.3; 6373 -7.8; 7010 -7.9; 7711 -10.0; 8482 -13.0; 9330 -13.2; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.45 | 6.1 dB  |
| Peaking | 74 Hz    | 3.78 | 1.2 dB  |
| Peaking | 200 Hz   | 0.55 | -2.9 dB |
| Peaking | 3927 Hz  | 2.24 | 1.3 dB  |
| Peaking | 8809 Hz  | 3.44 | -7.8 dB |
| Peaking | 1250 Hz  | 3.04 | 1.0 dB  |
| Peaking | 1843 Hz  | 4.22 | -1.2 dB |
| Peaking | 5041 Hz  | 9.15 | 1.8 dB  |
| Peaking | 5832 Hz  | 7.38 | -1.9 dB |
| Peaking | 11152 Hz | 6.28 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20600%20Ohm/Beyerdynamic%20DT%20880%20600%20Ohm.png)
# Beyerdynamic DT 880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.8; 41 -1.2; 45 -1.6; 49 -2.0; 54 -2.5; 60 -2.9; 66 -2.7; 72 -2.9; 79 -3.8; 87 -4.5; 96 -5.2; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.6; 155 -6.9; 170 -6.9; 187 -7.0; 206 -7.3; 227 -7.2; 249 -7.3; 274 -7.2; 302 -7.1; 332 -7.1; 365 -7.1; 402 -6.9; 442 -6.4; 486 -6.2; 535 -6.4; 588 -6.1; 647 -6.0; 712 -5.9; 783 -5.7; 861 -6.0; 947 -5.8; 1042 -5.4; 1146 -5.3; 1261 -4.8; 1387 -5.0; 1526 -5.3; 1678 -5.7; 1846 -5.9; 2031 -5.5; 2234 -4.8; 2457 -3.9; 2703 -3.6; 2973 -3.8; 3270 -4.7; 3597 -5.8; 3957 -5.8; 4353 -5.9; 4788 -5.6; 5267 -6.9; 5793 -8.0; 6373 -7.7; 7010 -8.3; 7711 -11.0; 8482 -13.1; 9330 -12.0; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.2; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.29 | 6.2 dB  |
| Peaking | 157 Hz   | 0.63 | -1.9 dB |
| Peaking | 1171 Hz  | 1.2  | 1.3 dB  |
| Peaking | 2768 Hz  | 2.52 | 3.0 dB  |
| Peaking | 8567 Hz  | 3.21 | -7.3 dB |
| Peaking | 1829 Hz  | 8.4  | -0.6 dB |
| Peaking | 4823 Hz  | 6.39 | 1.1 dB  |
| Peaking | 5741 Hz  | 6.16 | -1.2 dB |
| Peaking | 11137 Hz | 5.93 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)
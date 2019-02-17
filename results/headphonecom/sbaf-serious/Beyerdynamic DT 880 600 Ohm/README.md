# Beyerdynamic DT 880 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.6; 31 -1.9; 34 -2.2; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.4; 54 -3.7; 60 -4.0; 66 -4.3; 72 -4.6; 79 -4.3; 87 -4.2; 96 -5.5; 106 -6.2; 116 -6.6; 128 -6.9; 141 -7.4; 155 -7.5; 170 -7.6; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.6; 302 -7.5; 332 -7.4; 365 -7.2; 402 -6.9; 442 -6.7; 486 -6.2; 535 -6.1; 588 -6.0; 647 -5.6; 712 -5.3; 783 -4.7; 861 -4.8; 947 -5.1; 1042 -4.8; 1146 -4.3; 1261 -4.3; 1387 -4.7; 1526 -5.2; 1678 -5.5; 1846 -6.3; 2031 -6.0; 2234 -5.0; 2457 -4.6; 2703 -5.0; 2973 -5.0; 3270 -4.3; 3597 -3.0; 3957 -3.5; 4353 -4.6; 4788 -5.1; 5267 -5.8; 5793 -8.7; 6373 -8.1; 7010 -5.8; 7711 -8.8; 8482 -12.9; 9330 -13.4; 10263 -9.4; 11289 -5.2; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -7.3; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.26 | 5.0 dB  |
| Peaking | 204 Hz   | 0.72 | -3.1 dB |
| Peaking | 8924 Hz  | 2.85 | -7.8 dB |
| Peaking | 9844 Hz  | 3.02 | -2.9 dB |
| Peaking | 11103 Hz | 2.6  | 2.7 dB  |
| Peaking | 85 Hz    | 8.38 | 1.2 dB  |
| Peaking | 1188 Hz  | 1.9  | 1.0 dB  |
| Peaking | 1862 Hz  | 5.09 | -1.4 dB |
| Peaking | 3752 Hz  | 3.46 | 2.3 dB  |
| Peaking | 5892 Hz  | 8.49 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20600%20Ohm/Beyerdynamic%20DT%20880%20600%20Ohm.png)
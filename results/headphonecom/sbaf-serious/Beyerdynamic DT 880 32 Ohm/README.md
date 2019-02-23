# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.0; 45 -2.4; 49 -2.8; 54 -3.2; 60 -3.6; 66 -3.5; 72 -3.2; 79 -4.3; 87 -5.2; 96 -5.6; 106 -6.0; 116 -6.2; 128 -6.7; 141 -6.9; 155 -7.1; 170 -7.3; 187 -7.5; 206 -7.6; 227 -7.3; 249 -7.3; 274 -7.2; 302 -7.1; 332 -6.9; 365 -6.6; 402 -6.1; 442 -5.9; 486 -6.0; 535 -5.8; 588 -5.3; 647 -4.9; 712 -4.7; 783 -4.5; 861 -4.4; 947 -4.2; 1042 -4.1; 1146 -3.8; 1261 -3.4; 1387 -3.5; 1526 -4.3; 1678 -4.9; 1846 -5.3; 2031 -5.7; 2234 -5.4; 2457 -4.5; 2703 -4.2; 2973 -4.5; 3270 -5.4; 3597 -5.9; 3957 -6.4; 4353 -6.6; 4788 -6.2; 5267 -7.5; 5793 -10.9; 6373 -11.0; 7010 -9.6; 7711 -11.3; 8482 -13.9; 9330 -13.4; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.9  | 6.4 dB  |
| Peaking | 70 Hz    | 3.76 | 2.0 dB  |
| Peaking | 1333 Hz  | 0.69 | 2.6 dB  |
| Peaking | 6099 Hz  | 4.71 | -4.6 dB |
| Peaking | 8717 Hz  | 3.62 | -8.3 dB |
| Peaking | 50 Hz    | 3.3  | 0.8 dB  |
| Peaking | 204 Hz   | 1.25 | -1.4 dB |
| Peaking | 2004 Hz  | 3.85 | -1.4 dB |
| Peaking | 2731 Hz  | 3.41 | 1.5 dB  |
| Peaking | 10994 Hz | 6.57 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)
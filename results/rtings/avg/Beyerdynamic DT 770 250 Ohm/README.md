# Beyerdynamic DT 770 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.8; 28 -7.1; 31 -7.3; 34 -7.4; 37 -7.4; 41 -7.2; 45 -7.0; 49 -6.6; 54 -6.1; 60 -5.8; 66 -5.7; 72 -5.6; 79 -5.7; 87 -5.9; 96 -6.1; 106 -6.2; 116 -6.2; 128 -6.0; 141 -5.3; 155 -4.4; 170 -3.4; 187 -2.4; 206 -2.0; 227 -2.4; 249 -3.1; 274 -3.8; 302 -4.4; 332 -4.8; 365 -5.2; 402 -5.6; 442 -6.0; 486 -6.1; 535 -6.1; 588 -6.0; 647 -6.0; 712 -5.9; 783 -5.9; 861 -5.7; 947 -5.4; 1042 -5.1; 1146 -5.2; 1261 -5.8; 1387 -6.3; 1526 -6.7; 1678 -7.1; 1846 -7.6; 2031 -8.5; 2234 -8.9; 2457 -8.3; 2703 -6.6; 2973 -4.2; 3270 -0.9; 3597 -0.5; 3957 -5.7; 4353 -8.7; 4788 -7.5; 5267 -5.4; 5793 -6.4; 6373 -9.4; 7010 -9.4; 7711 -11.4; 8482 -14.0; 9330 -12.1; 10263 -7.5; 11289 -6.6; 12418 -9.5; 13660 -12.1; 15026 -11.4; 16529 -11.2; 18182 -14.7; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 213 Hz   | 2.04 | 4.2 dB   |
| Peaking | 2222 Hz  | 2.97 | -3.3 dB  |
| Peaking | 3387 Hz  | 5.65 | 7.3 dB   |
| Peaking | 8381 Hz  | 3.38 | -7.2 dB  |
| Peaking | 20335 Hz | 0.3  | -11.6 dB |
| Peaking | 34 Hz    | 2.02 | -1.6 dB  |
| Peaking | 1067 Hz  | 4.25 | 1.2 dB   |
| Peaking | 4367 Hz  | 9.99 | -3.2 dB  |
| Peaking | 11045 Hz | 5.42 | 3.3 dB   |
| Peaking | 13646 Hz | 4.19 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20770%20250%20Ohm/Beyerdynamic%20DT%20770%20250%20Ohm.png)
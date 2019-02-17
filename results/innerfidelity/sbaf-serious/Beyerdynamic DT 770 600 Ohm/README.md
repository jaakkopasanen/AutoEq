# Beyerdynamic DT 770 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.6; 25 -8.0; 28 -8.6; 31 -9.1; 34 -9.5; 37 -9.8; 41 -10.0; 45 -10.2; 49 -10.2; 54 -10.0; 60 -9.2; 66 -7.5; 72 -5.2; 79 -4.9; 87 -8.0; 96 -10.8; 106 -11.7; 116 -11.6; 128 -11.1; 141 -10.3; 155 -8.3; 170 -8.0; 187 -6.9; 206 -6.3; 227 -6.1; 249 -6.7; 274 -7.2; 302 -7.5; 332 -7.7; 365 -7.7; 402 -7.7; 442 -7.4; 486 -7.4; 535 -7.2; 588 -6.6; 647 -6.3; 712 -6.2; 783 -5.9; 861 -5.9; 947 -5.8; 1042 -5.6; 1146 -5.5; 1261 -5.8; 1387 -6.4; 1526 -6.8; 1678 -7.4; 1846 -7.6; 2031 -7.0; 2234 -7.5; 2457 -7.6; 2703 -6.7; 2973 -5.1; 3270 -3.6; 3597 -1.6; 3957 -1.3; 4353 -1.3; 4788 -0.5; 5267 -10.8; 5793 -12.8; 6373 -13.3; 7010 -11.4; 7711 -13.0; 8482 -15.8; 9330 -14.5; 10263 -9.0; 11289 -6.7; 12418 -9.8; 13660 -11.3; 15026 -9.0; 16529 -9.8; 18182 -13.7; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 116 Hz   | 1.37 | -5.6 dB  |
| Peaking | 4608 Hz  | 1.69 | 23.1 dB  |
| Peaking | 5434 Hz  | 1.05 | -20.6 dB |
| Peaking | 8738 Hz  | 5.6  | -6.6 dB  |
| Peaking | 18937 Hz | 0.81 | -8.4 dB  |
| Peaking | 42 Hz    | 1.09 | -4.3 dB  |
| Peaking | 76 Hz    | 4.83 | 5.5 dB   |
| Peaking | 412 Hz   | 2.19 | -1.8 dB  |
| Peaking | 3599 Hz  | 7.9  | 2.8 dB   |
| Peaking | 15947 Hz | 5.63 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB   |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)
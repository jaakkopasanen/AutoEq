# Beyerdynamic DT 880 32 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.7; 28 -0.9; 31 -1.2; 34 -1.3; 37 -1.4; 41 -1.6; 45 -1.7; 49 -1.8; 54 -2.0; 60 -2.2; 66 -2.6; 72 -2.9; 79 -3.4; 87 -3.9; 96 -4.4; 106 -4.9; 116 -5.4; 128 -5.8; 141 -6.2; 155 -6.5; 170 -6.7; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.8; 274 -6.8; 302 -6.9; 332 -6.9; 365 -6.9; 402 -7.2; 442 -7.4; 486 -7.2; 535 -7.1; 588 -7.2; 647 -7.1; 712 -6.9; 783 -7.0; 861 -6.8; 947 -6.6; 1042 -6.3; 1146 -6.0; 1261 -6.0; 1387 -6.0; 1526 -6.2; 1678 -7.1; 1846 -8.3; 2031 -8.8; 2234 -8.8; 2457 -8.3; 2703 -8.7; 2973 -8.8; 3270 -8.2; 3597 -6.8; 3957 -6.0; 4353 -6.2; 4788 -6.1; 5267 -7.4; 5793 -11.2; 6373 -12.1; 7010 -10.2; 7711 -12.8; 8482 -16.4; 9330 -15.9; 10263 -13.1; 11289 -12.2; 12418 -12.2; 13660 -12.0; 15026 -12.3; 16529 -14.3; 18182 -17.3; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 32 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.6  | 5.4 dB  |
| Peaking | 62 Hz    | 0.76 | 3.3 dB  |
| Peaking | 168 Hz   | 0.44 | -1.1 dB |
| Peaking | 2141 Hz  | 4.34 | -2.0 dB |
| Peaking | 20302 Hz | 0.07 | -9.3 dB |
| Peaking | 1359 Hz  | 2.28 | 1.5 dB  |
| Peaking | 4434 Hz  | 2.12 | 5.3 dB  |
| Peaking | 8877 Hz  | 4.99 | -5.0 dB |
| Peaking | 13909 Hz | 0.62 | 6.9 dB  |
| Peaking | 15911 Hz | 0.11 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 3.4 dB   |
| Peaking | 125 Hz   | 1.41 | 0.0 dB   |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -8.2 dB  |
| Peaking | 16000 Hz | 1.41 | -10.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)
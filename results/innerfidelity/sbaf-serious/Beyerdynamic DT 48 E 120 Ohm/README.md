# Beyerdynamic DT 48 E 120 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -2.1; 72 -9.6; 79 -14.2; 87 -11.6; 96 -9.8; 106 -11.2; 116 -10.7; 128 -10.1; 141 -9.6; 155 -8.7; 170 -9.3; 187 -9.2; 206 -8.7; 227 -8.0; 249 -7.5; 274 -6.8; 302 -6.2; 332 -5.8; 365 -5.4; 402 -4.7; 442 -3.8; 486 -3.0; 535 -1.8; 588 -0.7; 647 -1.0; 712 -2.1; 783 -3.7; 861 -5.1; 947 -6.0; 1042 -7.8; 1146 -9.8; 1261 -10.9; 1387 -11.7; 1526 -12.5; 1678 -13.4; 1846 -13.2; 2031 -12.9; 2234 -11.7; 2457 -8.9; 2703 -6.1; 2973 -4.9; 3270 -4.4; 3597 -2.8; 3957 -1.0; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.5; 7711 -12.2; 8482 -15.4; 9330 -12.3; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.6; 16529 -16.9; 18182 -17.9; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E 120 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E 120 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 1.67 | 7.5 dB   |
| Peaking | 1814 Hz  | 1.03 | -17.9 dB |
| Peaking | 4554 Hz  | 0.15 | 11.4 dB  |
| Peaking | 8486 Hz  | 2.8  | -17.2 dB |
| Peaking | 17460 Hz | 0.7  | -16.5 dB |
| Peaking | 61 Hz    | 2.18 | 7.8 dB   |
| Peaking | 78 Hz    | 4.36 | -10.9 dB |
| Peaking | 111 Hz   | 2.02 | -4.2 dB  |
| Peaking | 198 Hz   | 1.58 | -2.7 dB  |
| Peaking | 601 Hz   | 3.23 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -9.4 dB |
| Peaking | 4000 Hz  | 1.41 | 10.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -9.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20120%20Ohm/Beyerdynamic%20DT%2048%20E%20120%20Ohm.png)
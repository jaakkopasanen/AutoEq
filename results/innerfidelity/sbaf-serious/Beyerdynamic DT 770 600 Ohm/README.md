# Beyerdynamic DT 770 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.5; 25 -6.9; 28 -7.5; 31 -8.0; 34 -8.4; 37 -8.6; 41 -8.9; 45 -9.1; 49 -9.1; 54 -8.9; 60 -8.1; 66 -6.4; 72 -4.1; 79 -3.8; 87 -6.9; 96 -9.7; 106 -10.6; 116 -10.5; 128 -10.0; 141 -9.2; 155 -7.2; 170 -6.9; 187 -5.8; 206 -5.2; 227 -5.0; 249 -5.6; 274 -6.1; 302 -6.4; 332 -6.5; 365 -6.6; 402 -6.6; 442 -6.3; 486 -6.3; 535 -6.1; 588 -5.5; 647 -5.2; 712 -5.1; 783 -4.8; 861 -4.8; 947 -4.7; 1042 -4.5; 1146 -4.4; 1261 -4.7; 1387 -5.3; 1526 -5.7; 1678 -6.3; 1846 -6.5; 2031 -5.9; 2234 -6.4; 2457 -6.5; 2703 -5.6; 2973 -4.0; 3270 -2.5; 3597 -0.6; 3957 -0.5; 4353 -0.6; 4788 -0.5; 5267 -9.7; 5793 -11.7; 6373 -12.2; 7010 -10.3; 7711 -11.9; 8482 -14.7; 9330 -13.4; 10263 -7.9; 11289 -6.5; 12418 -8.7; 13660 -10.2; 15026 -7.9; 16529 -8.7; 18182 -12.6; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 3.41 | -4.8 dB  |
| Peaking | 4577 Hz  | 1.67 | 12.8 dB  |
| Peaking | 5660 Hz  | 2.2  | -12.8 dB |
| Peaking | 8666 Hz  | 3.77 | -8.3 dB  |
| Peaking | 18926 Hz | 0.81 | -6.5 dB  |
| Peaking | 56 Hz    | 0.87 | -3.1 dB  |
| Peaking | 75 Hz    | 4.08 | 6.3 dB   |
| Peaking | 212 Hz   | 3.47 | 2.0 dB   |
| Peaking | 954 Hz   | 1.41 | 1.9 dB   |
| Peaking | 2358 Hz  | 3.79 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)
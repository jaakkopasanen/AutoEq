# Beyerdynamic DT 48 S 5 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -1.2; 332 -2.9; 365 -4.8; 402 -6.6; 442 -8.2; 486 -10.3; 535 -12.6; 588 -14.5; 647 -16.7; 712 -17.9; 783 -18.3; 861 -18.1; 947 -17.9; 1042 -17.1; 1146 -16.4; 1261 -16.4; 1387 -16.7; 1526 -16.8; 1678 -17.7; 1846 -18.4; 2031 -17.7; 2234 -16.3; 2457 -13.5; 2703 -11.5; 2973 -8.9; 3270 -7.9; 3597 -7.5; 3957 -6.5; 4353 -6.3; 4788 -4.7; 5267 -3.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -11.1; 9330 -12.9; 10263 -12.2; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -8.9; 16529 -7.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 S 5 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 S 5 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.14 | 7.1 dB   |
| Peaking | 748 Hz   | 1.11 | -14.9 dB |
| Peaking | 1818 Hz  | 1.26 | -10.4 dB |
| Peaking | 6099 Hz  | 1.72 | 7.9 dB   |
| Peaking | 9186 Hz  | 2.36 | -8.5 dB  |
| Peaking | 21 Hz    | 2.62 | 1.1 dB   |
| Peaking | 284 Hz   | 3.3  | 2.5 dB   |
| Peaking | 510 Hz   | 3.3  | -1.4 dB  |
| Peaking | 3125 Hz  | 6.33 | 1.6 dB   |
| Peaking | 15575 Hz | 5.05 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.5 dB   |
| Peaking | 125 Hz   | 1.41 | 4.2 dB   |
| Peaking | 250 Hz   | 1.41 | 7.7 dB   |
| Peaking | 500 Hz   | 1.41 | -4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -10.5 dB |
| Peaking | 2000 Hz  | 1.41 | -10.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20S%205%20Ohm/Beyerdynamic%20DT%2048%20S%205%20Ohm.png)
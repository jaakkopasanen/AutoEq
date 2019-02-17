# Noontec Rio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.8; 23 -19.6; 25 -19.3; 28 -19.0; 31 -18.7; 34 -18.4; 37 -18.1; 41 -17.7; 45 -17.3; 49 -17.0; 54 -16.7; 60 -16.3; 66 -16.1; 72 -15.9; 79 -15.7; 87 -15.4; 96 -15.2; 106 -14.8; 116 -14.4; 128 -14.1; 141 -13.7; 155 -13.3; 170 -12.9; 187 -12.4; 206 -11.9; 227 -11.2; 249 -10.7; 274 -10.2; 302 -9.6; 332 -9.0; 365 -8.5; 402 -8.0; 442 -7.3; 486 -7.0; 535 -6.6; 588 -6.1; 647 -5.9; 712 -5.2; 783 -5.0; 861 -5.3; 947 -5.6; 1042 -6.1; 1146 -6.5; 1261 -7.0; 1387 -7.8; 1526 -8.6; 1678 -9.3; 1846 -9.7; 2031 -10.1; 2234 -10.7; 2457 -11.5; 2703 -12.5; 2973 -13.0; 3270 -12.3; 3597 -11.3; 3957 -12.8; 4353 -16.7; 4788 -15.3; 5267 -8.0; 5793 -2.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -6.5; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Rio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Rio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -13.5 dB |
| Peaking | 157 Hz   | 0.79 | -3.6 dB  |
| Peaking | 2719 Hz  | 1.36 | -6.2 dB  |
| Peaking | 4564 Hz  | 3.8  | -10.9 dB |
| Peaking | 6200 Hz  | 3.55 | 8.2 dB   |
| Peaking | 87 Hz    | 3.57 | -0.5 dB  |
| Peaking | 296 Hz   | 2.12 | -0.7 dB  |
| Peaking | 786 Hz   | 1.68 | 1.8 dB   |
| Peaking | 1623 Hz  | 3.77 | -1.3 dB  |
| Peaking | 17926 Hz | 4.04 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Rio/Noontec%20Rio.png)
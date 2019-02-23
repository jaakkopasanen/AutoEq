# Beyerdynamic T70 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.5; 28 -2.8; 31 -3.1; 34 -3.2; 37 -3.4; 41 -3.6; 45 -3.8; 49 -3.9; 54 -4.0; 60 -4.1; 66 -4.2; 72 -4.4; 79 -4.9; 87 -5.4; 96 -6.0; 106 -6.4; 116 -6.8; 128 -7.5; 141 -8.0; 155 -7.9; 170 -7.4; 187 -7.9; 206 -7.7; 227 -7.3; 249 -7.2; 274 -7.2; 302 -7.3; 332 -7.6; 365 -7.8; 402 -8.1; 442 -7.9; 486 -7.5; 535 -6.8; 588 -6.7; 647 -6.8; 712 -7.0; 783 -6.9; 861 -7.0; 947 -7.0; 1042 -7.0; 1146 -7.0; 1261 -7.0; 1387 -7.3; 1526 -7.5; 1678 -7.5; 1846 -6.9; 2031 -5.8; 2234 -3.7; 2457 -2.8; 2703 -3.4; 2973 -3.8; 3270 -4.0; 3597 -4.1; 3957 -0.5; 4353 -2.9; 4788 -3.5; 5267 -0.9; 5793 -0.5; 6373 -2.4; 7010 -7.7; 7711 -12.6; 8482 -15.5; 9330 -15.3; 10263 -11.6; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.77 | 4.2 dB   |
| Peaking | 3813 Hz  | 1.38 | 4.2 dB   |
| Peaking | 5531 Hz  | 4.56 | 3.4 dB   |
| Peaking | 6192 Hz  | 4.59 | 4.8 dB   |
| Peaking | 8687 Hz  | 2.55 | -11.0 dB |
| Peaking | 160 Hz   | 1.89 | -1.6 dB  |
| Peaking | 393 Hz   | 2.3  | -1.5 dB  |
| Peaking | 1961 Hz  | 1.08 | -2.3 dB  |
| Peaking | 2395 Hz  | 3.38 | 4.4 dB   |
| Peaking | 11641 Hz | 5.3  | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)
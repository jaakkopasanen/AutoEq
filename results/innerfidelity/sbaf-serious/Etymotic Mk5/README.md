# Etymotic Mk5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -0.9; 54 -1.2; 60 -1.6; 66 -2.0; 72 -2.3; 79 -2.7; 87 -3.2; 96 -3.7; 106 -4.1; 116 -4.3; 128 -4.6; 141 -4.8; 155 -5.0; 170 -5.2; 187 -5.4; 206 -5.4; 227 -5.5; 249 -5.6; 274 -5.5; 302 -5.4; 332 -5.3; 365 -5.3; 402 -5.4; 442 -5.1; 486 -5.2; 535 -5.2; 588 -5.0; 647 -5.0; 712 -5.3; 783 -5.4; 861 -6.0; 947 -6.7; 1042 -7.6; 1146 -8.4; 1261 -9.3; 1387 -10.5; 1526 -11.7; 1678 -12.7; 1846 -13.2; 2031 -13.5; 2234 -13.4; 2457 -12.3; 2703 -10.7; 2973 -8.7; 3270 -7.4; 3597 -7.9; 3957 -7.9; 4353 -6.5; 4788 -4.5; 5267 -3.7; 5793 -4.3; 6373 -4.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Mk5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Mk5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.4  | 6.3 dB  |
| Peaking | 658 Hz  | 0.82 | 1.9 dB  |
| Peaking | 1530 Hz | 1.53 | -3.3 dB |
| Peaking | 2146 Hz | 1.67 | -6.1 dB |
| Peaking | 5677 Hz | 2.08 | 3.4 dB  |
| Peaking | 3236 Hz | 6.96 | 1.1 dB  |
| Peaking | 3934 Hz | 7.44 | -1.2 dB |
| Peaking | 6875 Hz | 9.14 | 2.0 dB  |
| Peaking | 7631 Hz | 2.36 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20Mk5/Etymotic%20Mk5.png)
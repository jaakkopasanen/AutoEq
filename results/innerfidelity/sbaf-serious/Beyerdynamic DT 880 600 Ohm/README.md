# Beyerdynamic DT 880 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.3; 37 -1.7; 41 -2.1; 45 -2.4; 49 -2.7; 54 -3.1; 60 -3.6; 66 -3.8; 72 -3.5; 79 -4.1; 87 -5.2; 96 -5.8; 106 -6.2; 116 -6.5; 128 -7.0; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.8; 206 -7.9; 227 -7.9; 249 -7.9; 274 -7.7; 302 -7.6; 332 -7.5; 365 -7.3; 402 -7.2; 442 -6.7; 486 -6.5; 535 -6.6; 588 -6.3; 647 -6.2; 712 -6.1; 783 -5.7; 861 -5.8; 947 -5.5; 1042 -5.2; 1146 -4.9; 1261 -4.6; 1387 -5.0; 1526 -5.4; 1678 -6.0; 1846 -6.4; 2031 -6.0; 2234 -5.8; 2457 -4.9; 2703 -5.2; 2973 -4.9; 3270 -4.7; 3597 -4.3; 3957 -4.3; 4353 -5.0; 4788 -4.2; 5267 -4.4; 5793 -7.2; 6373 -6.7; 7010 -6.8; 7711 -8.9; 8482 -11.9; 9330 -12.1; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.11 | 6.3 dB  |
| Peaking | 56 Hz    | 1.85 | 2.3 dB  |
| Peaking | 1198 Hz  | 2.53 | 1.8 dB  |
| Peaking | 3915 Hz  | 1.27 | 2.3 dB  |
| Peaking | 8829 Hz  | 3.82 | -6.8 dB |
| Peaking | 76 Hz    | 5.3  | 1.5 dB  |
| Peaking | 210 Hz   | 0.98 | -1.6 dB |
| Peaking | 2483 Hz  | 8.73 | 0.6 dB  |
| Peaking | 9681 Hz  | 8.42 | -1.8 dB |
| Peaking | 10509 Hz | 3.96 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20600%20Ohm/Beyerdynamic%20DT%20880%20600%20Ohm.png)
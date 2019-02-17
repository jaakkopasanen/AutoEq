# House of Marley Legend
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.2; 25 -5.4; 28 -5.6; 31 -5.8; 34 -6.0; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.7; 54 -7.1; 60 -7.4; 66 -7.7; 72 -8.1; 79 -8.5; 87 -8.9; 96 -9.4; 106 -9.6; 116 -9.7; 128 -10.1; 141 -10.4; 155 -10.5; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.2; 302 -10.0; 332 -9.8; 365 -9.4; 402 -9.1; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.1; 647 -6.7; 712 -6.4; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.8; 1526 -8.3; 1678 -8.8; 1846 -8.7; 2031 -8.4; 2234 -7.7; 2457 -6.0; 2703 -4.9; 2973 -2.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Legend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Legend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.6  | 1.7 dB  |
| Peaking | 148 Hz  | 0.69 | -3.7 dB |
| Peaking | 305 Hz  | 1.35 | -2.0 dB |
| Peaking | 1952 Hz | 1.77 | -4.4 dB |
| Peaking | 4070 Hz | 1.02 | 7.2 dB  |
| Peaking | 804 Hz  | 2.15 | 1.1 dB  |
| Peaking | 2543 Hz | 0.14 | -0.3 dB |
| Peaking | 3193 Hz | 9.03 | 1.8 dB  |
| Peaking | 6334 Hz | 3.3  | 5.0 dB  |
| Peaking | 7233 Hz | 1.5  | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Legend/House%20of%20Marley%20Legend.png)
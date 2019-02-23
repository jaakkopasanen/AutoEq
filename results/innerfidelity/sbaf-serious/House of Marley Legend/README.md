# House of Marley Legend
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.4; 28 -6.7; 31 -6.9; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.1; 60 -8.5; 66 -8.7; 72 -9.2; 79 -9.5; 87 -10.0; 96 -10.4; 106 -10.7; 116 -10.7; 128 -11.1; 141 -11.4; 155 -11.5; 170 -11.7; 187 -11.7; 206 -11.7; 227 -11.5; 249 -11.5; 274 -11.3; 302 -11.1; 332 -10.8; 365 -10.5; 402 -10.1; 442 -9.6; 486 -9.4; 535 -8.9; 588 -8.2; 647 -7.7; 712 -7.5; 783 -7.2; 861 -7.3; 947 -7.4; 1042 -7.6; 1146 -7.9; 1261 -8.2; 1387 -8.8; 1526 -9.3; 1678 -9.8; 1846 -9.8; 2031 -9.4; 2234 -8.8; 2457 -7.0; 2703 -6.0; 2973 -3.6; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -2.1; 5793 -2.0; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Legend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Legend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 148 Hz  | 0.6  | -4.6 dB |
| Peaking | 327 Hz  | 1.09 | -2.3 dB |
| Peaking | 1955 Hz | 1.37 | -4.7 dB |
| Peaking | 3782 Hz | 1.46 | 7.6 dB  |
| Peaking | 6232 Hz | 4.97 | 3.8 dB  |
| Peaking | 17 Hz   | 1.28 | 0.8 dB  |
| Peaking | 1500 Hz | 5.22 | -0.3 dB |
| Peaking | 3954 Hz | 5.49 | -2.0 dB |
| Peaking | 4245 Hz | 1.98 | 1.3 dB  |
| Peaking | 8334 Hz | 2.5  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Legend/House%20of%20Marley%20Legend.png)
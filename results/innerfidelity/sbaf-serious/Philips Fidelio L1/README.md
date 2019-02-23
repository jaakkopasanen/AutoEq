# Philips Fidelio L1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.3; 25 -9.6; 28 -10.0; 31 -10.3; 34 -10.5; 37 -10.7; 41 -10.8; 45 -10.9; 49 -11.0; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.2; 87 -11.1; 96 -11.0; 106 -10.9; 116 -10.7; 128 -11.0; 141 -11.1; 155 -10.9; 170 -10.1; 187 -9.7; 206 -9.7; 227 -9.6; 249 -9.6; 274 -9.2; 302 -8.7; 332 -8.2; 365 -7.6; 402 -6.9; 442 -6.3; 486 -5.9; 535 -5.1; 588 -4.3; 647 -3.6; 712 -3.3; 783 -2.7; 861 -2.8; 947 -3.0; 1042 -3.0; 1146 -3.4; 1261 -4.1; 1387 -6.1; 1526 -8.2; 1678 -10.0; 1846 -10.7; 2031 -10.5; 2234 -11.1; 2457 -11.2; 2703 -10.3; 2973 -8.7; 3270 -6.1; 3597 -4.5; 3957 -3.3; 4353 -1.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.3; 7711 -7.0; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio L1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.36 | -4.2 dB |
| Peaking | 242 Hz  | 0.49 | -2.5 dB |
| Peaking | 1023 Hz | 0.66 | 7.3 dB  |
| Peaking | 2010 Hz | 0.96 | -9.0 dB |
| Peaking | 4939 Hz | 1.68 | 7.9 dB  |
| Peaking | 2844 Hz | 3.65 | -2.2 dB |
| Peaking | 3310 Hz | 1.86 | 2.1 dB  |
| Peaking | 4779 Hz | 2.2  | -1.3 dB |
| Peaking | 6377 Hz | 4.2  | 4.0 dB  |
| Peaking | 7423 Hz | 2.46 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)
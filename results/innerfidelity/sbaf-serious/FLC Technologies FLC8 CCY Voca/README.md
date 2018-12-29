# FLC Technologies FLC8 CCY Voca
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.8; 34 5.6; 37 5.5; 41 5.3; 45 5.0; 49 4.8; 54 4.5; 60 4.0; 66 3.6; 72 3.3; 79 2.7; 87 2.2; 96 1.7; 106 1.3; 116 1.1; 128 0.7; 141 0.3; 155 0.0; 170 -0.2; 187 -0.3; 206 -0.5; 227 -0.4; 249 -0.5; 274 -0.4; 302 -0.3; 332 -0.2; 365 -0.0; 402 0.1; 442 0.4; 486 0.4; 535 0.6; 588 1.1; 647 1.2; 712 1.1; 783 1.3; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.3; 1261 -2.5; 1387 -4.2; 1526 -6.1; 1678 -7.0; 1846 -5.9; 2031 -3.6; 2234 -2.2; 2457 -1.0; 2703 -0.6; 2973 -0.6; 3270 3.6; 3597 6.0; 3957 6.0; 4353 5.1; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -1.4; 10263 -2.5; 11289 -1.7; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 CCY Voca GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 CCY Voca ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.79 | 5.9 dB  |
| Peaking | 57 Hz   | 1.3  | 2.6 dB  |
| Peaking | 1722 Hz | 2.24 | -8.1 dB |
| Peaking | 4991 Hz | 1.04 | 7.3 dB  |
| Peaking | 9573 Hz | 1.7  | -3.9 dB |
| Peaking | 225 Hz  | 1.53 | -0.8 dB |
| Peaking | 741 Hz  | 1.81 | 1.8 dB  |
| Peaking | 3045 Hz | 3.97 | -4.4 dB |
| Peaking | 3433 Hz | 3.98 | 4.5 dB  |
| Peaking | 4494 Hz | 5.81 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20CCY%20Voca/FLC%20Technologies%20FLC8%20CCY%20Voca.png)
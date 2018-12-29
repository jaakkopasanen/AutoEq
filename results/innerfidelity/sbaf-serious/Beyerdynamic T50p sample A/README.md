# Beyerdynamic T50p sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.6; 49 5.0; 54 4.2; 60 3.4; 66 2.6; 72 2.0; 79 1.6; 87 1.2; 96 0.7; 106 1.4; 116 1.4; 128 1.8; 141 1.6; 155 2.2; 170 2.2; 187 0.5; 206 -1.4; 227 -2.2; 249 -2.5; 274 -2.4; 302 -2.6; 332 -2.6; 365 -2.6; 402 -2.6; 442 -2.4; 486 -2.4; 535 -2.1; 588 -1.5; 647 -1.4; 712 -1.2; 783 0.2; 861 0.2; 947 -0.0; 1042 0.2; 1146 0.5; 1261 0.7; 1387 0.6; 1526 0.3; 1678 0.2; 1846 0.9; 2031 2.1; 2234 4.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.54 | 6.7 dB  |
| Peaking | 158 Hz  | 1.64 | 5.6 dB  |
| Peaking | 216 Hz  | 0.53 | -4.6 dB |
| Peaking | 3017 Hz | 1.43 | 6.1 dB  |
| Peaking | 5384 Hz | 2.17 | 5.3 dB  |
| Peaking | 1249 Hz | 1.45 | 1.0 dB  |
| Peaking | 1721 Hz | 1.99 | -1.7 dB |
| Peaking | 2397 Hz | 6.97 | 1.9 dB  |
| Peaking | 6526 Hz | 6.01 | 2.7 dB  |
| Peaking | 7731 Hz | 2.02 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20A/Beyerdynamic%20T50p%20sample%20A.png)
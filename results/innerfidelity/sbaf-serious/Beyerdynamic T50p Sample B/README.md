# Beyerdynamic T50p sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.5; 41 5.0; 45 4.6; 49 4.2; 54 3.8; 60 3.2; 66 2.8; 72 2.5; 79 2.2; 87 1.8; 96 1.4; 106 2.3; 116 2.9; 128 2.4; 141 2.6; 155 3.1; 170 3.5; 187 1.8; 206 0.1; 227 -1.0; 249 -1.7; 274 -1.8; 302 -1.8; 332 -2.4; 365 -2.4; 402 -2.2; 442 -2.1; 486 -2.1; 535 -1.9; 588 -1.5; 647 -1.3; 712 -0.1; 783 -0.1; 861 -0.3; 947 -0.1; 1042 0.2; 1146 0.7; 1261 1.3; 1387 1.7; 1526 2.3; 1678 3.3; 1846 5.1; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.58 | 5.1 dB  |
| Peaking | 55 Hz   | 0.29 | 1.5 dB  |
| Peaking | 160 Hz  | 1.72 | 4.8 dB  |
| Peaking | 281 Hz  | 0.43 | -3.7 dB |
| Peaking | 3192 Hz | 0.64 | 7.0 dB  |
| Peaking | 81 Hz   | 4.64 | -0.2 dB |
| Peaking | 2039 Hz | 2.79 | 3.1 dB  |
| Peaking | 2230 Hz | 0.95 | -1.7 dB |
| Peaking | 6203 Hz | 2.07 | 5.7 dB  |
| Peaking | 7445 Hz | 1.42 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20B/Beyerdynamic%20T50p%20sample%20B.png)
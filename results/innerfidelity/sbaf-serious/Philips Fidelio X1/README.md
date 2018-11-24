# Philips Fidelio X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 3.0; 25 2.0; 28 0.7; 31 -0.5; 34 -1.6; 37 -2.6; 41 -3.8; 45 -4.8; 49 -5.7; 54 -6.5; 60 -7.1; 66 -7.4; 72 -7.5; 79 -7.5; 87 -7.4; 96 -7.4; 106 -7.0; 116 -6.5; 128 -6.3; 141 -6.1; 155 -5.8; 170 -5.4; 187 -6.2; 206 -5.7; 227 -5.0; 249 -4.6; 274 -4.2; 302 -3.8; 332 -3.5; 365 -3.1; 402 -2.8; 442 -2.4; 486 -2.5; 535 -2.2; 588 -1.8; 647 -1.7; 712 -1.7; 783 -1.4; 861 -0.9; 947 -0.2; 1042 0.1; 1146 0.4; 1261 0.5; 1387 -1.3; 1526 -2.7; 1678 -3.2; 1846 -3.0; 2031 -3.1; 2234 -2.9; 2457 -2.7; 2703 -0.8; 2973 1.1; 3270 -0.7; 3597 -1.8; 3957 -1.8; 4353 -3.0; 4788 -3.3; 5267 -2.9; 5793 -3.8; 6373 -2.3; 7010 -1.8; 7711 -3.6; 8482 -6.3; 9330 -5.9; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.88 | 6.4 dB  |
| Peaking | 65 Hz   | 0.62 | -7.2 dB |
| Peaking | 212 Hz  | 0.57 | -3.6 dB |
| Peaking | 1961 Hz | 2.06 | -3.3 dB |
| Peaking | 8422 Hz | 2.08 | -5.7 dB |
| Peaking | 1179 Hz | 5.53 | 1.9 dB  |
| Peaking | 2941 Hz | 7.83 | 3.3 dB  |
| Peaking | 5463 Hz | 1.15 | -4.9 dB |
| Peaking | 7981 Hz | 1.14 | 6.2 dB  |
| Peaking | 8972 Hz | 3.9  | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X1/Philips%20Fidelio%20X1.png)
# Philips Fidelio S1 Early 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -1.4; 23 -1.4; 25 -1.4; 28 -1.4; 31 -1.4; 34 -1.5; 37 -1.5; 41 -1.5; 45 -1.5; 49 -1.6; 54 -1.7; 60 -1.8; 66 -2.0; 72 -2.2; 79 -2.4; 87 -2.6; 96 -2.8; 106 -2.8; 116 -2.8; 128 -2.8; 141 -2.8; 155 -2.7; 170 -2.6; 187 -2.4; 206 -2.2; 227 -1.9; 249 -1.7; 274 -1.4; 302 -1.1; 332 -0.8; 365 -0.5; 402 -0.3; 442 0.1; 486 0.9; 535 0.5; 588 1.0; 647 1.1; 712 1.0; 783 1.1; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -2.8; 1678 -3.3; 1846 -3.4; 2031 -3.2; 2234 -2.8; 2457 -1.6; 2703 -0.5; 2973 0.9; 3270 2.0; 3597 2.0; 3957 0.3; 4353 -3.1; 4788 -4.8; 5267 -2.7; 5793 1.1; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio S1 Early 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S1 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 107 Hz  | 0.6  | -3.0 dB |
| Peaking | 1891 Hz | 2.05 | -3.9 dB |
| Peaking | 3527 Hz | 2.81 | 4.0 dB  |
| Peaking | 4735 Hz | 3.24 | -6.2 dB |
| Peaking | 6442 Hz | 4.63 | 5.1 dB  |
| Peaking | 23 Hz   | 1.45 | -1.2 dB |
| Peaking | 235 Hz  | 1.66 | -0.6 dB |
| Peaking | 681 Hz  | 1.2  | 1.6 dB  |
| Peaking | 1397 Hz | 3.11 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S1%20Early%202013/Philips%20Fidelio%20S1%20Early%202013.png)
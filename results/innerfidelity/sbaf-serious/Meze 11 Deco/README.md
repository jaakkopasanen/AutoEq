# Meze 11 Deco

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -11.7; 23 -11.7; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.9; 37 -11.9; 41 -11.9; 45 -11.9; 49 -12.0; 54 -12.0; 60 -12.1; 66 -12.2; 72 -12.4; 79 -12.5; 87 -12.6; 96 -12.7; 106 -12.7; 116 -12.5; 128 -12.4; 141 -12.3; 155 -12.0; 170 -11.7; 187 -11.3; 206 -10.8; 227 -10.2; 249 -9.7; 274 -9.1; 302 -8.4; 332 -7.8; 365 -7.0; 402 -6.4; 442 -5.4; 486 -4.9; 535 -4.1; 588 -3.3; 647 -2.0; 712 -1.7; 783 -0.4; 861 -0.2; 947 -0.2; 1042 0.1; 1146 0.3; 1261 0.4; 1387 0.2; 1526 -0.5; 1678 -2.5; 1846 -4.3; 2031 -3.9; 2234 -2.4; 2457 0.0; 2703 2.2; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.5; 4788 4.3; 5267 3.5; 5793 0.4; 6373 -7.1; 7010 -4.4; 7711 0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 11 Deco GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Deco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -10.7 dB |
| Peaking | 178 Hz   | 0.41 | -9.0 dB  |
| Peaking | 2060 Hz  | 1.72 | -13.0 dB |
| Peaking | 2758 Hz  | 0.57 | 10.3 dB  |
| Peaking | 6568 Hz  | 4.67 | -11.7 dB |
| Peaking | 800 Hz   | 9.73 | 1.0 dB   |
| Peaking | 1746 Hz  | 8.65 | -1.4 dB  |
| Peaking | 2641 Hz  | 7.81 | -1.4 dB  |
| Peaking | 5172 Hz  | 0.5  | 0.7 dB   |
| Peaking | 10359 Hz | 1.12 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Deco/Meze%2011%20Deco.png)
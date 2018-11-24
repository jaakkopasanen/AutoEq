# Bowers & Wilkins C5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -13.9; 23 -13.7; 25 -13.6; 28 -13.3; 31 -13.1; 34 -12.8; 37 -12.5; 41 -12.2; 45 -11.9; 49 -11.7; 54 -11.4; 60 -11.1; 66 -10.9; 72 -10.7; 79 -10.5; 87 -10.3; 96 -10.1; 106 -9.7; 116 -9.3; 128 -9.0; 141 -8.6; 155 -8.2; 170 -7.7; 187 -7.2; 206 -6.8; 227 -6.1; 249 -5.6; 274 -5.0; 302 -4.3; 332 -3.7; 365 -3.2; 402 -2.6; 442 -1.9; 486 -1.5; 535 -1.0; 588 -0.3; 647 0.1; 712 0.2; 783 0.6; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.4; 1387 -0.9; 1526 -1.6; 1678 -2.1; 1846 -2.3; 2031 -2.2; 2234 -2.4; 2457 -2.5; 2703 -3.0; 2973 -3.5; 3270 -3.6; 3597 -2.9; 3957 -2.9; 4353 -4.3; 4788 -4.8; 5267 -3.9; 5793 -3.1; 6373 -1.9; 7010 -0.6; 7711 -0.2; 8482 -0.5; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins C5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins C5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.6  | -10.2 dB |
| Peaking | 85 Hz   | 0.29 | -8.9 dB  |
| Peaking | 711 Hz  | 0.93 | 2.2 dB   |
| Peaking | 2616 Hz | 0.82 | -2.9 dB  |
| Peaking | 4901 Hz | 2.75 | -3.6 dB  |
| Peaking | 1703 Hz | 4.6  | -0.7 dB  |
| Peaking | 2443 Hz | 1.72 | 0.6 dB   |
| Peaking | 3071 Hz | 5.85 | -1.0 dB  |
| Peaking | 7522 Hz | 8.11 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20C5/Bowers%20&%20Wilkins%20C5.png)
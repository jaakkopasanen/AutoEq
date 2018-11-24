# Monster Inspiration

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 0.1; 25 -1.0; 28 -2.5; 31 -3.8; 34 -4.8; 37 -5.7; 41 -6.8; 45 -7.7; 49 -8.6; 54 -9.4; 60 -10.2; 66 -10.8; 72 -11.2; 79 -11.5; 87 -11.7; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.2; 141 -12.0; 155 -11.6; 170 -11.0; 187 -10.3; 206 -9.5; 227 -8.6; 249 -7.5; 274 -6.2; 302 -4.7; 332 -2.8; 365 -0.9; 402 0.3; 442 1.1; 486 3.1; 535 4.8; 588 5.0; 647 4.7; 712 3.7; 783 2.5; 861 1.5; 947 0.6; 1042 -0.3; 1146 -1.0; 1261 -2.2; 1387 -3.7; 1526 -5.0; 1678 -6.1; 1846 -7.1; 2031 -8.1; 2234 -9.2; 2457 -10.4; 2703 -11.7; 2973 -10.9; 3270 -9.5; 3597 -7.6; 3957 -6.3; 4353 -6.4; 4788 -7.6; 5267 -5.9; 5793 -0.4; 6373 5.5; 7010 1.6; 7711 -4.6; 8482 -7.6; 9330 -6.2; 10263 -3.1; 11289 -1.0; 12418 -2.6; 13660 -6.3; 15026 -7.6; 16529 -5.6; 18182 -0.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 0.78 | -11.0 dB |
| Peaking | 167 Hz   | 1.43 | -8.1 dB  |
| Peaking | 2432 Hz  | 1.69 | -9.0 dB  |
| Peaking | 3588 Hz  | 1.42 | -5.2 dB  |
| Peaking | 14897 Hz | 1.37 | -7.4 dB  |
| Peaking | 21 Hz    | 3.11 | 3.0 dB   |
| Peaking | 597 Hz   | 2.21 | 6.9 dB   |
| Peaking | 5282 Hz  | 3.8  | -6.6 dB  |
| Peaking | 6301 Hz  | 3.61 | 11.1 dB  |
| Peaking | 8443 Hz  | 4.03 | -8.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Monster%20Inspiration/Monster%20Inspiration.png)
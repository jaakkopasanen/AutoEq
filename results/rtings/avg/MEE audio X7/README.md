# MEE audio X7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 3.9; 37 3.6; 41 3.1; 45 2.8; 49 2.4; 54 2.0; 60 1.3; 66 0.6; 72 0.1; 79 -0.4; 87 -0.9; 96 -1.6; 106 -2.3; 116 -2.9; 128 -3.5; 141 -3.9; 155 -4.1; 170 -4.2; 187 -4.3; 206 -4.4; 227 -4.2; 249 -3.9; 274 -3.5; 302 -3.0; 332 -2.5; 365 -1.9; 402 -1.4; 442 -1.0; 486 -0.4; 535 0.3; 588 0.5; 647 0.7; 712 1.1; 783 1.2; 861 0.9; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.0; 1387 -1.2; 1526 -1.5; 1678 -1.9; 1846 -2.5; 2031 -3.0; 2234 -3.2; 2457 -3.6; 2703 -5.4; 2973 -8.0; 3270 -9.8; 3597 -10.6; 3957 -11.8; 4353 -14.7; 4788 -15.4; 5267 -9.3; 5793 -3.7; 6373 -1.4; 7010 -0.6; 7711 -2.2; 8482 -3.4; 9330 -0.9; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -4.8; 15026 -6.0; 16529 -5.6; 18182 -7.5; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.55 | 6.0 dB   |
| Peaking | 174 Hz   | 0.89 | -5.0 dB  |
| Peaking | 4205 Hz  | 1.8  | -15.0 dB |
| Peaking | 15203 Hz | 3.13 | -3.7 dB  |
| Peaking | 18541 Hz | 1.4  | -8.1 dB  |
| Peaking | 732 Hz   | 1.39 | 2.6 dB   |
| Peaking | 2769 Hz  | 0.09 | -0.9 dB  |
| Peaking | 4891 Hz  | 9.6  | -4.7 dB  |
| Peaking | 6340 Hz  | 2.86 | 4.5 dB   |
| Peaking | 11173 Hz | 3.11 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X7/MEE%20audio%20X7.png)
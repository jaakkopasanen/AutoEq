# Beats Solo3 Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.0; 49 -7.1; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.7; 79 -7.8; 87 -8.0; 96 -8.2; 106 -8.3; 116 -8.4; 128 -8.5; 141 -8.4; 155 -8.4; 170 -8.2; 187 -7.9; 206 -7.4; 227 -6.9; 249 -6.3; 274 -5.5; 302 -4.7; 332 -4.1; 365 -3.4; 402 -2.9; 442 -3.0; 486 -2.4; 535 -1.6; 588 -0.8; 647 0.0; 712 0.6; 783 0.9; 861 0.8; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.9; 1387 -2.6; 1526 -3.0; 1678 -3.5; 1846 -4.1; 2031 -4.1; 2234 -3.8; 2457 -3.5; 2703 -4.4; 2973 -5.9; 3270 -7.0; 3597 -7.8; 3957 -5.6; 4353 -4.8; 4788 -5.7; 5267 -4.0; 5793 -2.9; 6373 -4.3; 7010 -4.7; 7711 -3.8; 8482 -4.5; 9330 -4.9; 10263 -3.1; 11289 -1.5; 12418 -2.4; 13660 -4.1; 15026 -3.0; 16529 -0.1; 18182 -0.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.32 | -6.5 dB |
| Peaking | 136 Hz   | 0.85 | -4.7 dB |
| Peaking | 242 Hz   | 1.25 | -3.1 dB |
| Peaking | 3265 Hz  | 0.93 | -5.6 dB |
| Peaking | 9890 Hz  | 0.54 | -3.1 dB |
| Peaking | 837 Hz   | 2.33 | 2.5 dB  |
| Peaking | 1852 Hz  | 1.02 | -1.7 dB |
| Peaking | 2493 Hz  | 3.78 | 2.7 dB  |
| Peaking | 17530 Hz | 3.16 | 1.7 dB  |
| Peaking | 20047 Hz | 3.39 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)